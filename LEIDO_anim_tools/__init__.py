import bpy
from .tools import tool_visibility
from .tools import tool_weight_transfer

bl_info = {
    "name" : "LEIDO Tools",
    "author" : "kev-fbx",
    "description": "Tools that help with the LEIDO workflow",
    "blender": (3, 0, 0),
    "version": (0, 1, 0),
    "location": "3D View > Properties > LEIDO",
    "warning": "",
    "category": "Animation",
}

classes = (
    tool_visibility.VISIBILITY_OT_keyframe_visibility_hide,
    tool_visibility.VISIBILITY_OT_keyframe_visibility_show,
    tool_weight_transfer.transfer_weights,
    tool_weight_transfer.WEIGHT_TRANSFER_PT_ui,
    tool_visibility.VISIBILITY_PT_keyframe_visibility_ui,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)