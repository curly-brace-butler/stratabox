# Setting Up Your StrataBox Controller

This guide will walk you through installing CircuitPython on your Raspberry Pi Pico and deploying the StrataBox code.

## Installing CircuitPython

1. **Download CircuitPython for Raspberry Pi Pico**
   - Visit the [CircuitPython website](https://circuitpython.org/board/raspberry_pi_pico/)
   - Download the latest UF2 file for the Raspberry Pi Pico

2. **Connect Pico in Bootloader Mode**
   - Hold down the BOOTSEL button on your Pico
   - While holding BOOTSEL, connect the Pico to your computer via USB
   - Release the BOOTSEL button after connecting

3. **Install CircuitPython**
   - Your Pico should appear as a USB drive named "RPI-RP2"
   - Drag and drop the downloaded UF2 file onto this drive
   - The Pico will automatically restart and reconnect as a new drive named "CIRCUITPY"

## Deploying StrataBox Code

1. **Install Required Libraries**
   - Create a new folder called `lib` in the CIRCUITPY drive
   - Download the [CircuitPython libraries bundle](https://circuitpython.org/libraries)
   - From the bundle, extract and copy the `adafruit_hid` folder to the `lib` folder on your Pico

2. **Copy StrataBox Files**
   - Copy these files to the root of the CIRCUITPY drive:
     - `boot.py`
     - `code.py`
     - `config.py`
     - `debug_probe_utils.py` (optional)
   
3. **That's it!**
   - The code runs automatically when the files are copied
   - The device will restart and start running the code immediately
   - You should see the startup LED sequence if everything is working

## Troubleshooting

- **Pico not appearing as CIRCUITPY drive**
  - Try another USB cable (some cables are power-only)
  - Try another USB port on your computer
  
- **CircuitPython not running**
  - Check that `code.py` is in the root directory of CIRCUITPY
  - Ensure the `adafruit_hid` library is correctly installed in the lib folder

- **Buttons not working**
  - Double-check your wiring connections
  - Try running `button_test.py` (rename it to `code.py` temporarily)

## Reference

CircuitPython works as a simple drag-and-drop system:

1. The Pico appears as a USB drive called CIRCUITPY
2. Files copied to this drive are immediately accessible to the Pico
3. The `code.py` file runs automatically on startup
4. Changes to files are detected and the device resets to use them

You can use the serial console (115200 baud) for debugging output. 