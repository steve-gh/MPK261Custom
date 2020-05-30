from __future__ import absolute_import, print_function, unicode_literals
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.DeviceComponent import DeviceComponent
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.MixerComponent import MixerComponent
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder, make_slider
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from .SessionComponent import SessionComponent
from .TransportComponent import TransportComponent

SESSION_WIDTH = 4
SESSION_HEIGHT = 7


class MidiMap(MidiMapBase):

    def add_multi_channel_matrix(self, name, element_factory, numbers, midi_message_type):
        """Add a matrix across multiple channels.
            numbers: A tuple (channel, midi-number)
        """
        assert name not in self.keys()

        def one_dimensional_name(base_name, x, _y):
            return u'%s[%d]' % (base_name, x)

        def two_dimensional_name(base_name, x, y):
            return u'%s[%d,%d]' % (base_name, x, y)

        name_factory = two_dimensional_name if len(numbers) > 1 else one_dimensional_name
        elements = [[element_factory(name_factory(name, column, row),
                                     identifier[0], identifier[1], midi_message_type)
                     for column, identifier in enumerate(identifiers)]
                    for row, identifiers in enumerate(numbers)]
        self[name] = ButtonMatrixElement(rows=elements)


    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        self.add_button(u'Play', 0, 118, MIDI_CC_TYPE)
        self.add_button(u'Record', 0, 119, MIDI_CC_TYPE)
        self.add_button(u'Stop', 0, 117, MIDI_CC_TYPE)
        self.add_button(u'Loop', 0, 114, MIDI_CC_TYPE)
        self.add_button(u'Forward', 0, 116, MIDI_CC_TYPE)
        self.add_button(u'Backward', 0, 115, MIDI_CC_TYPE)
        self.add_matrix(u'Sliders', make_slider, 0,
                        [[12, 13, 14, 15, 16, 17, 18, 19]],
                        MIDI_CC_TYPE)
        self.add_matrix(u'Encoders', make_encoder, 0,
                        [[22, 23, 24, 25, 26, 27, 28, 29]],
                        MIDI_CC_TYPE)

        self.add_matrix(u'Arm_Buttons', make_button, 0,
                        [[32, 33, 34, 35, 36, 37, 38, 39]],
                        MIDI_CC_TYPE)

        # Control bank "B" knobs.
        self.add_matrix(u'EncodersB1', make_encoder, 1,
                        [[22, 23, 24, 25, 26, 27, 28, 29]],
                        MIDI_CC_TYPE)

        # Control bank "B" buttons
        # MPK261 LiveLite default is "momentary" which sends "on" when button is
        # pressed and "off" when button is released.
        # To change to toggle - go to Edit, pg2 (right arrow)
        #  change mode from Momentary to Toggle
        #  repeat for S1 through S8
        #  save by going preset -> right arrow -> enter to save
        self.add_matrix(u'Mute_Buttons', make_button, 1,
                        [[32, 33, 34, 35, 36, 37, 38, 39]],
                        MIDI_CC_TYPE)

        # Control bank "C" buttons
        # S1 bank C
        self.add_button(u'Metronome', 2, 32, MIDI_CC_TYPE)
        # S2 bank C
        self.add_button(u'TapTempoButton', 2, 33, MIDI_CC_TYPE)
        # S3 bank C
        self.add_button(u'RecQuantButton', 2, 34, MIDI_CC_TYPE)
        # S4 bank C
        self.add_button(u'OverdubButton', 2, 35, MIDI_CC_TYPE)


        # Existing drum pads (Bank A), don't change them.
        self.add_matrix(u'Drum_Pads', make_button, 1,
                        [[81, 83, 84, 86],
                         [74, 76, 77, 79],
                         [67, 69, 71, 72],
                         [60, 62, 64, 65]],
                        MIDI_NOTE_TYPE)

        # Pad Banks C & Banks D, for clip launching
        # channel, midi-number
        self.add_multi_channel_matrix(u'Drum_Pads_BankB', make_button, [
            [(2, 81), (2, 83), (2, 84), (2, 86)],
            [(2, 74), (2, 76), (2, 77), (2, 79)],
            [(2, 67), (2, 69), (2, 71), (2, 72)],
            [(2, 60), (2, 62), (2, 64), (2, 65)],
            [(3, 81), (3, 83), (3, 84), (3, 86)],
            [(3, 74), (3, 76), (3, 77), (3, 79)],
            [(3, 67), (3, 69), (3, 71), (3, 72)]
            ], MIDI_NOTE_TYPE)

        # BankD
        # Pad Button 15 -> scene launch 1
        # Pad Button 11 -> scene launch 2
        # Pad Button  7 -> scene launch 3
        # Pad Button  3 -> scene launch 4
        # Pad Button 16 -> scene launch 5
        # Pad Button 12 -> scene launch 6
        # Pad Button 18 -> scene launch 7
        self.add_matrix(u'Drum_Pads_BankD_RightColumn', make_button, 4,
                        [[84, 77, 71, 64, 86, 79, 72]], MIDI_NOTE_TYPE)

        # BankC, pad 1-4, for clip stop
        self.add_matrix(u'Drum_Pads_BankC_BottomRow', make_button, 3,
                        [[60, 62, 64, 65]], MIDI_NOTE_TYPE)


class MPK261Custom(ControlSurface):

    def __init__(self, *a, **k):
        super(MPK261Custom, self).__init__(*a, **k)
        with self.component_guard():
            midimap = MidiMap()
            drum_rack = DrumRackComponent(name=u'Drum_Rack', is_enabled=False,
                                          layer=Layer(pads=midimap[u'Drum_Pads']))
            drum_rack.set_enabled(True)
            transport = TransportComponent(name=u'Transport', is_enabled=False, layer=Layer(
                play_button=midimap[u'Play'],
                record_button=midimap[u'Record'],
                stop_button=midimap[u'Stop'],
                seek_forward_button=midimap[u'Forward'],
                seek_backward_button=midimap[u'Backward'],
                loop_button=midimap[u'Loop'],
                metronome_button=midimap[u'Metronome'],
                tap_tempo_button=midimap[u'TapTempoButton'],
                quant_toggle_button=midimap[u'RecQuantButton'],
                overdub_button=midimap[u'OverdubButton']
                ))
            transport.set_enabled(True)
            mixer_size = len(midimap[u'Sliders'])

            # Custom changes: Adds the "mute" buttons. By default, mute = turns light on.
            # invert_mute_feedback flips it around so muting = turns light off.
            mixer = MixerComponent(mixer_size, name=u'Mixer', is_enabled=False,
                                   invert_mute_feedback=True,
                                   layer=Layer(
                                       volume_controls=midimap[u'Sliders'],
                                       pan_controls=midimap[u'Encoders'],
                                       arm_buttons=midimap[u'Arm_Buttons'],
                                       mute_buttons=midimap[u'Mute_Buttons'],
                                   ))
            mixer.set_enabled(True)

            # Adds the blue hand controls.
            device = DeviceComponent(
                name=u'Device', is_enabled=False,
                layer=Layer(parameter_controls=midimap[u'EncodersB1']),
                device_selection_follows_track_selection=True)
            device.set_enabled(True)
            self.set_device_component(device)

            session = SessionComponent(
                SESSION_WIDTH, SESSION_HEIGHT, auto_name=True, enable_skinning=True,
                is_enabled=False, layer=Layer(
                    clip_launch_buttons=midimap[u'Drum_Pads_BankB'],
                    stop_track_clip_buttons=midimap[u'Drum_Pads_BankC_BottomRow'],
                    scene_launch_buttons=midimap[u'Drum_Pads_BankD_RightColumn']))
            session.set_enabled(True)

        self.log_message(u' ***** MPK261 Custom script loaded ****')
