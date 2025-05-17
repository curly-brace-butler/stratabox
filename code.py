"""
StrataBox - Helldivers Arcade Button Controller
Circuit Python code for a Raspberry Pi Pico that emulates a USB keyboard
for controlling Helldivers with arcade buttons.
"""

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Try to import config, use defaults if not available
try:
    import config
    PIN_CONFIG = config.PIN_CONFIG
    KEY_CONFIG = config.KEY_CONFIG
    DEBOUNCE_TIME = config.DEBOUNCE_TIME
    LED_ENABLED = config.LED_ENABLED
    PRINT_DEBUG = config.PRINT_DEBUG
except ImportError:
    # Default configuration if config.py is not found
    PIN_CONFIG = {
        "MENU_BTN_PIN": board.GP15,
        "UP_BTN_PIN": board.GP16,
        "DOWN_BTN_PIN": board.GP17,
        "LEFT_BTN_PIN": board.GP18,
        "RIGHT_BTN_PIN": board.GP19,
    }
    KEY_CONFIG = {
        "MENU_KEY": Keycode.P,
        "UP_KEY": Keycode.UP_ARROW,
        "DOWN_KEY": Keycode.DOWN_ARROW,
        "LEFT_KEY": Keycode.LEFT_ARROW,
        "RIGHT_KEY": Keycode.RIGHT_ARROW,
    }
    DEBOUNCE_TIME = 0.05
    LED_ENABLED = True
    PRINT_DEBUG = True
    
    if PRINT_DEBUG:
        print("No config.py found, using default settings")

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Initialize button objects with pull-up resistors
menu_btn = digitalio.DigitalInOut(PIN_CONFIG["MENU_BTN_PIN"])
menu_btn.direction = digitalio.Direction.INPUT
menu_btn.pull = digitalio.Pull.UP

up_btn = digitalio.DigitalInOut(PIN_CONFIG["UP_BTN_PIN"])
up_btn.direction = digitalio.Direction.INPUT
up_btn.pull = digitalio.Pull.UP

down_btn = digitalio.DigitalInOut(PIN_CONFIG["DOWN_BTN_PIN"])
down_btn.direction = digitalio.Direction.INPUT
down_btn.pull = digitalio.Pull.UP

left_btn = digitalio.DigitalInOut(PIN_CONFIG["LEFT_BTN_PIN"])
left_btn.direction = digitalio.Direction.INPUT
left_btn.pull = digitalio.Pull.UP

right_btn = digitalio.DigitalInOut(PIN_CONFIG["RIGHT_BTN_PIN"])
right_btn.direction = digitalio.Direction.INPUT
right_btn.pull = digitalio.Pull.UP

# Create a list of buttons and their corresponding keycodes
buttons = [
    {"button": menu_btn, "keycode": KEY_CONFIG["MENU_KEY"], "state": True, "last_press_time": 0},
    {"button": up_btn, "keycode": KEY_CONFIG["UP_KEY"], "state": True, "last_press_time": 0},
    {"button": down_btn, "keycode": KEY_CONFIG["DOWN_KEY"], "state": True, "last_press_time": 0},
    {"button": left_btn, "keycode": KEY_CONFIG["LEFT_KEY"], "state": True, "last_press_time": 0},
    {"button": right_btn, "keycode": KEY_CONFIG["RIGHT_KEY"], "state": True, "last_press_time": 0},
]

# LED pin for status indicator
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Helper function for LED control
def set_led(value):
    if LED_ENABLED:
        led.value = value

# Blink the LED to show the device is ready
for _ in range(3):
    set_led(True)
    time.sleep(0.1)
    set_led(False)
    time.sleep(0.1)

if PRINT_DEBUG:
    print("StrataBox initialized and ready")
    print("This is the simplified version - for the true Helldivers experience!")
    print("Each button sends exactly one keystroke to the computer:")
    print("- Menu Button: P (opens stratagem menu)")
    print("- Four direction buttons: Arrow keys (for manual stratagem input)")

# Wait for stable button reading
time.sleep(0.5)  # Increased delay for stability

# Boot mode detection
sos_mode = not up_btn.value  # SOS mode if UP held at boot
default_menu_key = Keycode.P
practice_mode = not menu_btn.value  # Practice mode if MENU held at boot
if practice_mode:
    menu_key = Keycode.R
else:
    menu_key = default_menu_key

if PRINT_DEBUG:
    if sos_mode:
        print("SOS Mode activated - Emergency sequence available!")
    if practice_mode:
        print("Practice Mode activated - Menu button sends 'R' instead of 'P'")

# Update buttons list with correct menu key
buttons = [
    {"button": menu_btn, "keycode": menu_key, "state": True, "last_press_time": 0},
    {"button": up_btn, "keycode": KEY_CONFIG["UP_KEY"], "state": True, "last_press_time": 0},
    {"button": down_btn, "keycode": KEY_CONFIG["DOWN_KEY"], "state": True, "last_press_time": 0},
    {"button": left_btn, "keycode": KEY_CONFIG["LEFT_KEY"], "state": True, "last_press_time": 0},
    {"button": right_btn, "keycode": KEY_CONFIG["RIGHT_KEY"], "state": True, "last_press_time": 0},
]

# Add a counter for menu button presses
menu_press_count = 0
menu_press_time = 0
MENU_PRESS_TIMEOUT = 1.0  # Time window in seconds for three presses

while True:
    # Check each button
    for btn_data in buttons:
        current_state = btn_data["button"].value
        if current_state == False and btn_data["state"] == True:
            current_time = time.monotonic()
            if current_time - btn_data["last_press_time"] > DEBOUNCE_TIME:
                if PRINT_DEBUG:
                    print(f"Button pressed: {btn_data['keycode']}")
                set_led(True)
                kbd.press(btn_data["keycode"])
                time.sleep(0.01)
                kbd.release(btn_data["keycode"])
                btn_data["last_press_time"] = current_time
                set_led(False)
                # Check if menu button was pressed
                if btn_data["button"] == menu_btn:
                    if current_time - menu_press_time > MENU_PRESS_TIMEOUT:
                        menu_press_count = 1
                    else:
                        menu_press_count += 1
                    menu_press_time = current_time
                    if menu_press_count >= 3:
                        if sos_mode:  # Only trigger SOS sequence if SOS mode was activated at boot
                            if PRINT_DEBUG:
                                print("SOS macro triggered - Menu button pressed three times")
                            # Ensure the third P is sent before SOS sequence
                            time.sleep(0.05)
                            # Send arrow key sequence: up>down>right>left>up
                            sequence = [Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW]
                            for key in sequence:
                                kbd.press(key)
                                time.sleep(0.01)
                                kbd.release(key)
                                time.sleep(0.05)
                        menu_press_count = 0
        btn_data["state"] = current_state
    time.sleep(0.01) 