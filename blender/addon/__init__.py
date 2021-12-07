bl_info = {
    "name": "DMod Addon",
    "author": "Constantine Nisidis",
    "description":"",
    "version": (0,1),
    "blender": (2, 90, 0),
    "support": "TESTING",
    "category": "Tools"
}

import bpy
import os

#os.system('cls')

from op import DMOD
from ui import DMOD_PT_SETTINGS, DMOD_Settings





classes = (
    DMOD,
    DMOD_PT_SETTINGS,
    DMOD_Settings
)

register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
    register_classes()
    bpy.types.Scene.dModSettings =  bpy.props.PointerProperty(type=DMOD_Settings)
    
def unregister():
    unregister_classes()
    del bpy.types.Scene.dModSettings

print("DMOD Addon was loaded properly")