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

class VISIBILITY_PT_keyframe_visibility_ui(bpy.types.Panel):
    """UI Panel for visibility keyframing"""
    bl_label = "Visibility Keyframer"
    bl_idname = "VISIBILITY_PT_Visibility_Keyframer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LEIDO"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()

        row = layout.row(align=True)
        layout.operator("view3d.keyframe_visibility_show", text="Show in render")
        layout.operator("view3d.keyframe_visibility_hide", text="Hide in render")

class WEIGHT_TRANSFER_PT_ui(bpy.types.Panel):
    """UI panel for weight transfer"""
    bl_label = "Weight Transfer"
    bl_idname = "VIEW3D_PT_Weight_Transfer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "LEIDO"

    def draw(self, context):
        """Define the layout of the panel"""
        layout = self.layout
        scene = context.scene
        row = layout.row()
        
        row = layout.row(align=True)
        layout.operator("view3d.transfer_weights")

classes = (
    tool_visibility.VISIBILITY_OT_keyframe_visibility_hide,
    tool_visibility.VISIBILITY_OT_keyframe_visibility_show,
    tool_weight_transfer.transfer_weights,
    VISIBILITY_PT_keyframe_visibility_ui,
    WEIGHT_TRANSFER_PT_ui,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)