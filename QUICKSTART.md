# StrataBox Quick Start Guide

This guide will help you quickly set up and use your StrataBox controller for Helldivers.

## Setup Steps

1. **Install CircuitPython on your Raspberry Pi Pico**
   - Connect your Pico while holding the BOOTSEL button
   - Drag and drop the CircuitPython UF2 file to the RPI-RP2 drive
   - The Pico will restart and mount as CIRCUITPY

2. **Install Required Libraries**
   - Create a 'lib' folder on the CIRCUITPY drive
   - Copy the 'adafruit_hid' folder from the CircuitPython library bundle to the lib folder

3. **Copy Project Files**
   - Copy the following files to the root of the CIRCUITPY drive:
     - `code.py` (main program)
     - `config.py` (optional for customization)
     - `button_test.py` (for testing your buttons)

4. **Wire Your Buttons**
   - Connect each arcade button to the Pico according to WIRING.md
   - Default pin configuration:
     - Menu Button (P key): GP15
     - Up Arrow: GP16
     - Down Arrow: GP17
     - Left Arrow: GP18
     - Right Arrow: GP19
   - All buttons share a common ground connection to the Pico's GND pin

## Testing

1. **Rename button_test.py to code.py** to test your button connections
   ```
   # On your computer, rename the files on the CIRCUITPY drive
   Rename: code.py -> code.py.backup
   Rename: button_test.py -> code.py
   ```

2. **Press each button** to verify they're correctly wired
   - The Pico's LED should flash when a button is pressed
   - The console should display which button was pressed

3. **Restore the main code** when testing is complete
   ```
   # On your computer, rename the files back
   Rename: code.py -> button_test.py
   Rename: code.py.backup -> code.py
   ```

## Using the Controller

1. **Connect the StrataBox to your computer** via USB

2. **Launch Helldivers**

3. **Play the game with manual stratagem input:**
   - Press the Menu Button (P) to open the stratagem wheel
   - Manually execute each stratagem pattern using the direction buttons
   - Each button press corresponds to exactly one keystroke

## Playing Tips

- Learn the stratagem patterns by heart for faster execution
- The manual input method preserves the intended challenge and satisfaction
- Practice the timing of your button presses for smoother stratagem execution
- Enjoy the tactile feedback of arcade buttons while playing

## Customization

Edit the `config.py` file to:
- Change GPIO pin assignments if your wiring is different
- Remap button functions if desired
- Adjust debounce settings if you're experiencing multiple keypresses

Safely eject the CIRCUITPY drive after making changes for them to take effect. 