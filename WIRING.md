# StrataBox Wiring Guide

This guide explains how to wire the Sanwa arcade buttons to your Raspberry Pi Pico for the StrataBox project.

## Materials Needed
- Raspberry Pi Pico
- 5 Sanwa arcade buttons
- Hookup wire (preferably different colors for easier identification)
- Soldering equipment (optional but recommended for reliability)
- Mini USB cable for power and connecting to PC

## Wiring Diagram

```
Raspberry Pi Pico                          Arcade Buttons
+---------------+                        +----------------+
|               |                        |                |
|           GP15|-------------------------| Menu Button (P)|
|               |                        |                |
|           GP16|-------------------------| Up Button     |
|               |                        |                |
|           GP17|-------------------------| Down Button   |
|               |                        |                |
|           GP18|-------------------------| Left Button   |
|               |                        |                |
|           GP19|-------------------------| Right Button  |
|               |                        |                |
|            GND|--------+------+------+-| All Buttons GND|
|               |        |      |      | |                |
+---------------+        |      |      | +----------------+
                         |      |      |
                         +------+------+
                         (GND connections)
```

## Connection Instructions

1. **GPIO Connections (Signal Wires)**
   - Connect Menu Button (P) signal wire to GP15
   - Connect Up Button signal wire to GP16
   - Connect Down Button signal wire to GP17
   - Connect Left Button signal wire to GP18
   - Connect Right Button signal wire to GP19

2. **Ground Connections**
   - Connect the second wire from each arcade button to one of the GND pins on the Pico
   - You can daisy-chain the ground connections from button to button, ending at the Pico's GND pin

## Notes

- The code uses internal pull-up resistors, so no external resistors are needed
- Sanwa arcade buttons are mechanical switches that close a circuit when pressed
- The buttons are wired in an active-low configuration (they register as pressed when the signal is pulled to ground)
- If you're experiencing "bounce" issues (multiple keypresses detected from a single press), try increasing the `DEBOUNCE_TIME` in the code.py file

## Pin Configuration Table

| Button Function | Pico GPIO Pin | Connection Type |
|-----------------|---------------|----------------|
| Menu (P key)    | GP15          | Signal         |
| Up Arrow        | GP16          | Signal         |
| Down Arrow      | GP17          | Signal         |
| Left Arrow      | GP18          | Signal         |
| Right Arrow     | GP19          | Signal         |
| All Buttons     | GND           | Ground         | 