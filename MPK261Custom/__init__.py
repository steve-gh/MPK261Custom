from __future__ import absolute_import, print_function, unicode_literals
from .MPK261Custom import MPK261Custom
from _Framework.Capabilities import controller_id, inport, outport, CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, REMOTE

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[37], model_name=u'MPK261Custom'),
            PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT, REMOTE]), outport(props=[SCRIPT, REMOTE])]}


def create_instance(c_instance):
    return MPK261Custom(c_instance)
