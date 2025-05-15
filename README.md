# StrataBox

A Raspberry Pi Pico-based USB keyboard device for Helldivers using arcade buttons.

## Overview
StrataBox is a custom controller built with a Raspberry Pi Pico and Sanwa arcade buttons to help players execute stratagems in Helldivers. The device emulates a USB keyboard, sending specific keystrokes when buttons are pressed.

Unlike "macro" controllers that automate stratagem sequences, StrataBox preserves the core gameplay experience by having players manually input the directional commands - just as the game designers intended! It simply maps arcade buttons to the P key and arrow keys for a more tactile and satisfying experience.

## Hardware
- Raspberry Pi Pico
- 5 Sanwa arcade buttons:
  - 1 button for opening the stratagem menu (P key)
  - 4 directional buttons (Up, Down, Left, Right arrows)

## Wiring
Each arcade button connects to the Pico with two wires:
- One wire connects to a GPIO pin on the Pico (signal)
- The other wire connects to ground

## Software
The device runs CircuitPython and uses the HID library to emulate a USB keyboard. When buttons are pressed, the corresponding keystrokes are sent to the computer.

## Installation
1. Install CircuitPython on your Raspberry Pi Pico
2. Copy the `code.py` file to the Pico
3. Copy the required libraries to the `/lib` directory on the Pico

## Usage
1. Connect the StrataBox to your computer via USB
2. The device will be recognized as a USB keyboard
3. Press the buttons to trigger the corresponding keys:
   - Main button: P (opens stratagem menu)
   - Four directional buttons: Arrow keys (Up, Down, Left, Right)
4. To execute a stratagem:
   - Press the P button to open the stratagem menu
   - Manually input the sequence using the directional buttons
   - Experience the satisfaction of a well-executed stratagem sequence!

## Advanced Features

### USB Device Identification
The StrataBox now presents itself to your computer as "StrataBox Controller" instead of a generic "CIRCUITPY" device, making it easier to identify when connected. The device also performs a distinctive LED blink pattern on startup to confirm it's working properly.

### Raspberry Pi Debug Probe Support
If you own a Raspberry Pi Debug Probe, you can connect it to the Pico's SWD pins for advanced diagnostics:
- Monitor precise button timing to optimize debounce settings
- Test USB HID connectivity
- Generate comprehensive debug reports
- Access the REPL console while the device is functioning as a keyboard

To use the Debug Probe:
1. Connect the Debug Probe to the SWD pins on the Pico
2. Run the included debug_probe_utils.py utilities via the REPL console

## Future Enhancements
A potential enhancement for a future version is a "practice mode" that would use the onboard LED to help players learn stratagem patterns. This mode would flash the LED in patterns corresponding to specific stratagems, allowing players to practice the sequences without needing to be in-game.