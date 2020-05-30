from __future__ import absolute_import, print_function, unicode_literals
from _Framework.Control import ButtonControl
from _Framework.SessionComponent import SessionComponent as SessionComponentBase

class SessionComponent(SessionComponentBase):
    u""" Special SessionComponent with a button (pedal) to fire the selected clip slot """
    slot_launch_button = ButtonControl()

    def set_slot_launch_button(self, button):
        self.slot_launch_button.set_control_element(button)

    @slot_launch_button.pressed
    def slot_launch_button(self, button):
        clip_slot = self.song().view.highlighted_clip_slot
        if clip_slot:
            clip_slot.fire()
