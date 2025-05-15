# StrataBox Installation Guide

This guide walks you through setting up your Raspberry Pi Pico with CircuitPython and installing the necessary libraries for the StrataBox project.

## 1. Install CircuitPython on your Raspberry Pi Pico

1. Download the latest CircuitPython UF2 file for Raspberry Pi Pico from the [CircuitPython website](https://circuitpython.org/board/raspberry_pi_pico/).

2. Connect your Raspberry Pi Pico to your computer while holding down the BOOTSEL button on the Pico.

3. Release the BOOTSEL button after connecting. The Pico should mount as a USB drive named "RPI-RP2".

4. Drag and drop the downloaded CircuitPython UF2 file onto the RPI-RP2 drive.

5. The Pico will automatically restart and should now mount as a new drive named "CIRCUITPY".

## 2. Install Required Libraries

1. Download the CircuitPython HID library bundle from the [CircuitPython Libraries page](https://circuitpython.org/libraries).

2. Unzip the downloaded bundle.

3. From the unzipped files, locate and copy the following folders to the `/lib` directory on your CIRCUITPY drive:
   - `adafruit_hid`

   If the `/lib` directory doesn't exist on your CIRCUITPY drive, create it first.

## 3. Install the StrataBox Code

1. Copy the `code.py` file from this repository to the root of your CIRCUITPY drive.

2. Safely eject the CIRCUITPY drive.

3. The Pico will automatically restart and run the code.

## 4. Testing Your Installation

1. Reconnect your Pico to your computer.

2. The onboard LED should blink three times to indicate the device is ready.

3. Open a text editor or any application where keyboard input is accepted.

4. Press each of your arcade buttons to verify they send the correct keypresses:
   - Menu Button: Should type the letter "P"
   - Direction Buttons: Should send the corresponding arrow key presses

## Troubleshooting

- If no keypresses are detected:
  - Check that your buttons are correctly wired according to the WIRING.md guide
  - Ensure that the code.py file is properly copied to the root of the CIRCUITPY drive

- If you see multiple keypresses when pressing a button once:
  - Edit the code.py file and increase the DEBOUNCE_TIME value (e.g., from 0.05 to 0.1)

- If the Pico is not recognized as a USB keyboard:
  - Make sure you have installed the adafruit_hid library correctly
  - Try restarting your computer

## Further Resources

- [CircuitPython HID Documentation](https://docs.circuitpython.org/projects/hid/en/latest/)
- [Raspberry Pi Pico Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
- [CircuitPython Getting Started Guide](https://learn.adafruit.com/welcome-to-circuitpython) 