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

## MPK261 Mappings

For reference, here are the MPK261 MIDI button / CC mappings used in the MPK261 preset "LiveLite" and is what this is based on.

|Description                    |Label on keyboard        |MIDI CC|Comments                                                                                                                          |
|:-----------------------------:|:-----------------------:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------:|
|            Slider             |           F1            |  12   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F2            |  13   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F3            |  14   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F4            |  15   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F5            |  16   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F6            |  17   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F7            |  18   |                                            values 0-127, "channel" is "control bank"                                             |
|            Slider             |           F8            |  19   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K1            |  22   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K2            |  23   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K3            |  24   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K4            |  25   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K5            |  26   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K6            |  27   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K7            |  28   |                                            values 0-127, "channel" is "control bank"                                             |
|             Knob              |           K8            |  29   |                                            values 0-127, "channel" is "control bank"                                             |
|            Button             |           S1            |  32   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S2            |  33   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S3            |  34   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S4            |  35   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S5            |  36   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S6            |  37   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S7            |  38   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |           S8            |  39   |                                value 127 when pressed, 0 when released, channel is "control bank"                                |
|            Button             |         Rewind          |  115  |                                                127 when pressed, channel always 1                                                |
|            Button             |       FastForward       |  116  |                                                127 when pressed, channel always 1                                                |
|            Button             |          Stop           |  117  |                  127 when pressed, channel always 1. When pressed repeatedly sends a "note off" for all notes.                   |
|            Button             |          Play           |  118  |                                                127 when pressed, channel always 1                                                |
|            Button             |         Record          |  119  |                                                127 when pressed, channel always 1                                                |
|            Button             |          Loop           |  114  |                                                127 when pressed, channel always 1                                                |
|           Keyboard            |          Keys           |       |                     Top 2 notes (B & C on physical keyboard, regardless of which octave) - always Channel 2                      |
|           Keyboard            |          Keys           |       |                                C-2 (lowest) to C8 (highest). Channel 1 (except for top two notes)                                |
|              Pad              |          Pad 1          |  60   |Bank A -> Channel 2; Bank B->Channel 3; Bank C -> Channel4; Bank D -> Channel5.  Keyboard always Channel 1. Octave doesn't change.|
|              Pad              |          Pad 2          |  62   |                                                                                                                                  |
|              Pad              |          Pad 3          |  64   |                                                                                                                                  |
|              Pad              |          Pad 4          |  64   |                                                                                                                                  |
|              Pad              |   Pad 5 (2nd row up)    |  67   |                                                                                                                                  |
|              Pad              |          Pad 6          |  69   |                                                                                                                                  |
|              Pad              |          Pad 7          |  71   |                                                                                                                                  |
|              Pad              |          Pad 8          |  72   |                                                                                                                                  |
|              Pad              |   Pad 9 (3rd row up)    |  74   |                                                                                                                                  |
|              Pad              |         Pad 10          |  76   |                                                                                                                                  |
|              Pad              |         Pad 11          |  77   |                                                                                                                                  |
|              Pad              |         Pad 12          |  79   |                                                                                                                                  |
|              Pad              |Pad 13 (4th row up, left)|  81   |                                                                                                                                  |
|              Pad              |         Pad 14          |  83   |                                                                                                                                  |
|              Pad              |         Pad 15          |  84   |                                                                                                                                  |
|              Pad              |         Pad 16          |  86   |                                                                                                                                  |
|          Pitch Wheel          |                         |       |                                    From -8192 to 8192. Sends on both Channel 1 and Channel 2.                                    |
|Modulator (next to pitch wheel)|                         |   1   |                                               From 0 to 127 (middle is approx 63))                                               |
|         Sustain Pedal         |                         |  64   |                                                127 when pressed, 0 when released                                                 |


## Author

Steve Padgett / ableton@wreck.net

This is a work in progress, feel free to fork / send patches / etc.
