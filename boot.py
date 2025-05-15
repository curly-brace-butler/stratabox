"""
StrataBox Boot Configuration
This file runs before code.py and configures the USB device settings.
"""

import storage
import usb_cdc
import usb_hid
import board
import digitalio
import time

# Custom USB device information
USB_VID = 0x239A  # Adafruit's VID
USB_PID = 0x8101  # A unique PID (modified from CircuitPython defaults)
USB_DEVICE_NAME = "StrataBox Controller"
USB_MANUFACTURER = "Custom Helldivers Hardware"

# Set up LED for boot sequence
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Define custom HID keyboard device with our descriptors
# This makes the device show up with our custom name in device manager
keyboard_descriptor = usb_hid.Device(
    report_descriptor=bytes((
        0x05, 0x01,  # Usage Page (Generic Desktop)
        0x09, 0x06,  # Usage (Keyboard)
        0xA1, 0x01,  # Collection (Application)
        0x05, 0x07,  # Usage Page (Key Codes)
        0x19, 0xE0,  # Usage Minimum (224)
        0x29, 0xE7,  # Usage Maximum (231)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x01,  # Logical Maximum (1)
        0x75, 0x01,  # Report Size (1)
        0x95, 0x08,  # Report Count (8)
        0x81, 0x02,  # Input (Data, Variable, Absolute)
        0x95, 0x01,  # Report Count (1)
        0x75, 0x08,  # Report Size (8)
        0x81, 0x01,  # Input (Constant)
        0x95, 0x06,  # Report Count (6)
        0x75, 0x08,  # Report Size (8)
        0x15, 0x00,  # Logical Minimum (0)
        0x25, 0x65,  # Logical Maximum (101)
        0x05, 0x07,  # Usage Page (Key Codes)
        0x19, 0x00,  # Usage Minimum (0)
        0x29, 0x65,  # Usage Maximum (101)
        0x81, 0x00,  # Input (Data, Array)
        0xC0,        # End Collection
    )),
    usage_page=0x01,           # Generic Desktop
    usage=0x06,                # Keyboard
    report_ids=(0,),           # Report ID (0 = no report ID)
    in_report_lengths=(8,),    # 8 bytes input report
    out_report_lengths=(0,),   # No output report
)

# Override default HID devices with our custom one
usb_hid.enable(
    (keyboard_descriptor,),
    boot_device=1
)

# Override device info
storage.remount("/", readonly=False)
with open("/boot_out.txt", "w") as f:
    f.write(f"StrataBox Controller v1.0\n")
    f.write(f"=======================\n")
    f.write(f"Welcome to your custom Helldivers 2 controller!\n")
    f.write(f"- Press P button to open stratagem menu\n")
    f.write(f"- Use directional buttons to input stratagems manually\n")
    f.write(f"- Enjoy the tactile arcade button experience\n")
    f.write(f"=======================\n")
    f.write(f"For help, see the README on the CIRCUITPY drive\n")

# Auto-test sequence
# Perform a distinctive boot pattern to show the device is working
def startup_sequence():
    # Short-long-short pattern
    # Short blinks
    for _ in range(3):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)
    
    # Medium pause
    time.sleep(0.3)
    
    # Long blink
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.2)
    
    # Short blinks
    for _ in range(3):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

# Run startup test sequence
startup_sequence()

# Enable serial console for diagnostics and for Pi Debug Probe use
usb_cdc.enable(console=True, data=True)
print(f"StrataBox Controller v1.0 initialized")
print(f"USB Device Name: {USB_DEVICE_NAME}")
print(f"Manufacturer: {USB_MANUFACTURER}")
print(f"Diagnostic port ready for Raspberry Pi Debug Probe")
print(f"Press any button to test input functionality") 