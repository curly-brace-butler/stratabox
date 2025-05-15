"""
StrataBox Button Test Utility
Use this script to test if your buttons are correctly wired before using
the main keyboard emulation program.
"""

import time
import board
import digitalio

# Try to import config, use defaults if not available
try:
    import config
    PIN_CONFIG = config.PIN_CONFIG
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
    LED_ENABLED = True
    PRINT_DEBUG = True
    
    if PRINT_DEBUG:
        print("No config.py found, using default settings")

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

# Setup LED for visual feedback
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Helper function for LED control
def set_led(value):
    if LED_ENABLED:
        led.value = value

# Create a list of buttons with their names
buttons = [
    {"button": menu_btn, "name": "MENU (P key)", "state": True},
    {"button": up_btn, "name": "UP ARROW", "state": True},
    {"button": down_btn, "name": "DOWN ARROW", "state": True},
    {"button": left_btn, "name": "LEFT ARROW", "state": True},
    {"button": right_btn, "name": "RIGHT ARROW", "state": True},
]

# Blink LED 3 times to show program has started
for _ in range(3):
    set_led(True)
    time.sleep(0.2)
    set_led(False)
    time.sleep(0.2)

if PRINT_DEBUG:
    print("\n=== StrataBox Button Test Utility ===")
    print("Press each button to test if it's correctly wired.")
    print("Press Ctrl+C to exit\n")

try:
    while True:
        button_pressed = False
        
        # Check each button
        for btn_data in buttons:
            # Buttons are pulled up, so they read True when not pressed
            # and False when pressed
            current_state = btn_data["button"].value
            
            # If button state changed from not pressed to pressed
            if current_state == False and btn_data["state"] == True:
                if PRINT_DEBUG:
                    print(f"Button pressed: {btn_data['name']}")
                
                # Flash LED when button is pressed
                set_led(True)
                time.sleep(0.1)
                set_led(False)
                
                button_pressed = True
                
            # Update button state
            btn_data["state"] = current_state
        
        # If no button was pressed, keep the LED off
        if not button_pressed:
            set_led(False)
        
        # Small delay to avoid excessive CPU usage
        time.sleep(0.01)
        
except KeyboardInterrupt:
    if PRINT_DEBUG:
        print("\nTest finished.")
    
    # Final LED blink to indicate program end
    for _ in range(5):
        set_led(True)
        time.sleep(0.1)
        set_led(False)
        time.sleep(0.1) 