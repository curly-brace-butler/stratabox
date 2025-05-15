"""
StrataBox Configuration File
Edit this file to customize button mappings and other settings.
Save this file to your Raspberry Pi Pico as config.py.
"""

import board
from adafruit_hid.keycode import Keycode

# Button GPIO pin configuration
# Change these values to match your specific wiring
PIN_CONFIG = {
    "MENU_BTN_PIN": board.GP15,    # Button to open stratagem menu
    "UP_BTN_PIN": board.GP16,      # Up arrow button
    "DOWN_BTN_PIN": board.GP17,    # Down arrow button
    "LEFT_BTN_PIN": board.GP18,    # Left arrow button
    "RIGHT_BTN_PIN": board.GP19,   # Right arrow button
}

# Button key mappings
# Change these to remap buttons to different keys
KEY_CONFIG = {
    "MENU_KEY": Keycode.P,         # Default: P key
    "UP_KEY": Keycode.UP_ARROW,    # Default: Up arrow key
    "DOWN_KEY": Keycode.DOWN_ARROW, # Default: Down arrow key
    "LEFT_KEY": Keycode.LEFT_ARROW, # Default: Left arrow key
    "RIGHT_KEY": Keycode.RIGHT_ARROW, # Default: Right arrow key
}

# Other settings
DEBOUNCE_TIME = 0.05  # Time in seconds to debounce button presses
LED_ENABLED = True    # Set to False to disable LED feedback
PRINT_DEBUG = True    # Set to False to disable debug print statements 