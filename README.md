# Ableton Remote Script - MPK261Custom

This script adds a number of Ableton control functions for the Akai MPK261.
Ableton is a fantastic software suite, and the Akai MP261 is an excellent keyboard.
But the default MPK261 control in Ableton is lacking - it could do so much more!

## MPK261 Pre-Setup

To use effectively, a few defaults need to be changed in the MPK261 configuration.

### MPK261 Configuration Changes Required

This is based on the LiveLite default preset. Recommend creating a copy of this preset and editing that in the MPK261 config.

- Edit the Pads in banks B, C, and D Note Mode to use Toggle instead of Momentary.
  Momentary turns on the button while it is pressed and turns it off when it is released.
  Toggle turns the button on when pressed, then turns the button off when it is pressed a second time. To edit:
    1. Click the Edit button on the MPK261
    2. Click the correct Bank, then touch the Pad. The MPK261 display should show "Pad#" at the top.
    3. Click the right arrow 2 times to go to Pg3. The MPK261 display should show "Node Mode"
    4. Turn the knob to select "Toggle"
    5. Repeat for all the pads on banks B, C, and D. Touch the pad
- Edit the S1-S8 buttons for Control banks B & C to use Toggle instead of Momentary.
    1. Click the Edit button on the MPK261
    2. Click the correct Bank, then touch the S button (example: S1). The MPK261 display should show "Switch#" at the top.  Bank 2 switch 1 = Switch09, etc.
    3. Click the right arrow and down to go to Mode.
    4. Turn the knob to select "Toggle" from "Momentary"
    5. Repeat for all the switch buttons in control banks B & C.

## Ableton Mappings

![Overview](mpk261-mappings.png?raw=true)

### Pads
- Bank A - unchanged (drum pads)
- **Bank B (all pads) & C (top 3 pads) is Clip Launch for Sessions 1-7 (up/down) and Clips 1-4 (left/right).**
- **Bank C bottom pad is Clip Stop for Clips 1-4 (left/right)**
- **Bank D pads on the right-hand side (starting row 3 going down - pads 15, 11, 7, 3, 16, 12, 8) is Scene Launch 1-7**

### Knobs K1 - K8
- Control Bank A - Unchanged (pan left/right)
- **Control Bank B - Ableton Control "Blue Hand"**
- Control Bank C - Unchanged (Unassigned), open for custom bindings

### Sliders F1 - F8
- Control Bank A - Unchanged (Volume)
- Control Bank B - Unchanged (Unassigned), open for custom bindings
- Control Bank C - Unchanged (Unassigned), open for custom bindings

### Switches S1 - S8 (Buttons)
- Control Bank A - Unchanged (Select + Arm for recording)
- **Control Bank B - Mute. When light is on, track is unmuted. When light off, track is muted.**
- **Control Bank C**  Note - sometimes it appears these buttons take 2 presses.  Not clear why yet.
    - **C S1 - Metronome**
    - **C S2 - Tap for tempo**
    - **C S3 - Record with quantization**
    - **C S4 - Overdub on/off**
    - C S5 - S8 - Unassigned, open for custom bindings

## Installation

1. Use the Ableton installation instructions for [Installing third-party remote scripts](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts) which provides the directories and the general process.
2. Download the python files into a new directory, "MPK261Custom" under your "User Library" folder
   while Ableton is stopped. You may have to create the "User Library" directory.
   See the step above for how to do that and where it goes.
3. Start Ableton.  THe first time Ableton runs - and any time there is a change to a py file - it will compile the .py files into .pyc.
4. Under the preferences->Midi, choose MPK261Custom in the Control Surface.

## Troubleshooting

On the Mac, Ableton writes logs to:
/Users/{username}/Library/Preferences/Ableton/Live {version}/Log.txt

Python errors & other issues will be reported there.

## Author

Steve Padgett / ableton@wreck.net

This is a work in progress, feel free to fork / send patches / etc.
