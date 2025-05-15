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

while True:
    # Check each button
    for btn_data in buttons:
        # Buttons are pulled up, so they read True when not pressed
        # and False when pressed
        current_state = btn_data["button"].value
        
        # If button state changed from not pressed to pressed
        if current_state == False and btn_data["state"] == True:
            current_time = time.monotonic()
            
            # Debounce check
            if current_time - btn_data["last_press_time"] > DEBOUNCE_TIME:
                if PRINT_DEBUG:
                    print(f"Button pressed: {btn_data['keycode']}")
                
                # Flash LED when button is pressed
                set_led(True)
                
                # Send keypress
                kbd.press(btn_data["keycode"])
                time.sleep(0.01)  # Short delay for the key to register
                kbd.release(btn_data["keycode"])
                
                # Update last press time for debouncing
                btn_data["last_press_time"] = current_time
                
                # Turn off LED
                set_led(False)
                
        # Update button state
        btn_data["state"] = current_state
    
    # Small delay to avoid excessive CPU usage
    time.sleep(0.01) 