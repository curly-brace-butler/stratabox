"""
StrataBox Debug Probe Utilities
This file contains utilities for using a Raspberry Pi Debug Probe with the StrataBox.
Connect your Debug Probe to the StrataBox using the SWD pins.
"""

import time
import board
import digitalio

# Debug message function that outputs to both serial console and LED
def debug_message(message, blink_count=1):
    """
    Print a debug message and blink the LED to visually confirm.
    
    Args:
        message: The message to print to serial console
        blink_count: Number of times to blink the LED
    """
    print(f"DEBUG: {message}")
    
    # Blink the LED to visually confirm
    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    
    for _ in range(blink_count):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

# Function to monitor button states and report detailed timing
def monitor_button_timing(duration=10):
    """
    Monitor button presses and report detailed timing information.
    This is useful for debugging latency issues.
    
    Args:
        duration: How long to monitor in seconds
    """
    from code import buttons  # Import the buttons from the main code
    
    print(f"Beginning button timing monitor for {duration} seconds")
    print("Press buttons to see detailed timing information")
    
    start_time = time.monotonic()
    end_time = start_time + duration
    
    # Dictionary to track button states
    button_states = {}
    for btn in buttons:
        button_states[id(btn["button"])] = btn["button"].value
    
    while time.monotonic() < end_time:
        current_time = time.monotonic()
        
        # Check each button
        for btn in buttons:
            button_id = id(btn["button"])
            current_state = btn["button"].value
            
            # If button state changed from not pressed to pressed
            if current_state == False and button_states[button_id] == True:
                # Calculate and print response time
                event_time = time.monotonic()
                print(f"Button: {btn.get('direction', 'unknown')}")
                print(f"  Press detected at: {event_time - start_time:.6f}s")
                print(f"  Value: {current_state}")
            
            # Update button state
            button_states[button_id] = current_state
        
        # Small delay to avoid excessive CPU usage
        time.sleep(0.001)  # Use a smaller delay for more precise timing
    
    print("Button timing monitor completed")

# Function to test USB HID communication
def test_usb_hid_connection():
    """
    Test the USB HID connection by sending a test keystroke
    and checking for success.
    """
    import usb_hid
    from adafruit_hid.keyboard import Keyboard
    
    print("Testing USB HID connection...")
    
    try:
        # Initialize keyboard
        kbd = Keyboard(usb_hid.devices)
        
        # Print connection information
        print(f"HID devices available: {len(usb_hid.devices)}")
        for i, device in enumerate(usb_hid.devices):
            print(f"Device {i}: Usage Page: {device.usage_page}, Usage: {device.usage}")
        
        print("USB HID connection test complete")
        print("Connection is working properly")
        
        # Blink LED to indicate success
        led = digitalio.DigitalInOut(board.LED)
        led.direction = digitalio.Direction.OUTPUT
        for _ in range(3):
            led.value = True
            time.sleep(0.1)
            led.value = False
            time.sleep(0.1)
            
        return True
        
    except Exception as e:
        print(f"USB HID test failed: {e}")
        return False

# Function to capture and log a debug report for troubleshooting
def capture_debug_report():
    """
    Capture system information and create a debug report.
    """
    import os
    import microcontroller
    import gc
    
    debug_report = []
    debug_report.append("StrataBox Debug Report")
    debug_report.append("====================")
    
    # System information
    debug_report.append(f"CircuitPython version: {os.uname().version}")
    debug_report.append(f"Board: {os.uname().machine}")
    
    # Memory information
    gc.collect()
    debug_report.append(f"Free memory: {gc.mem_free()} bytes")
    debug_report.append(f"Allocated memory: {gc.mem_alloc()} bytes")
    
    # CPU temperature
    try:
        cpu_temp = microcontroller.cpu.temperature
        debug_report.append(f"CPU temperature: {cpu_temp:.1f}°C")
    except:
        debug_report.append("CPU temperature: Not available")
    
    # USB information
    try:
        debug_report.append(f"USB devices: {len(usb_hid.devices)}")
    except:
        debug_report.append("USB devices: Not available")
    
    # File system information
    try:
        debug_report.append("Files on device:")
        files = os.listdir("/")
        for file in files:
            try:
                file_stat = os.stat("/" + file)
                debug_report.append(f"  {file} ({file_stat[6]} bytes)")
            except:
                debug_report.append(f"  {file} (unknown size)")
    except:
        debug_report.append("File listing failed")
    
    # Join all lines and return
    report_text = "\n".join(debug_report)
    print(report_text)
    
    # Save to file if possible
    try:
        with open("/debug_report.txt", "w") as f:
            f.write(report_text)
        print("Debug report saved to /debug_report.txt")
    except:
        print("Could not save debug report to file")
    
    return report_text

# Example usage for Debug Probe console
if __name__ == "__main__":
    print("StrataBox Debug Utilities")
    print("========================")
    print("Available commands:")
    print("1. debug_message('message') - Print a debug message with LED confirmation")
    print("2. monitor_button_timing(duration) - Monitor button timing for latency testing")
    print("3. test_usb_hid_connection() - Test USB HID functionality")
    print("4. capture_debug_report() - Generate a complete system report")
    print("Use these functions via the Debug Probe REPL") 