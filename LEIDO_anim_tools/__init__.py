import bpy
import tools.tool_visibility as tool_visibility
import tools.tool_weight_transfer as tool_weight_transfer

bl_info = {
    "name" : "LEIDO Tools",
    "author" : "kev-fbx",
    "description": "Tools that help with the LEIDO workflow",
    "blender": (3, 0, 0),
    "version": (0, 1, 0),
    "location": "3D View > Properties > Tool",
    "warning": "",
    "category": "Animation",
}

class TOOLS_PT_LEIDO_Panel(bpy.types.Panel):
    """Panel for Visibility and Weight Tools"""
    bl_label = "Visibility & Weight Tools"
    bl_idname = "TOOLS_PT_visibility_weight_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Render Visibility:")
        row = layout.row(align=True)
        row.operator("object.keyframe_visibility_show", text="Show in Render")
        row.operator("object.keyframe_visibility_hide", text="Hide in Render")
        layout.separator()
        layout.label(text="Vertex Weight Transfer:")
        layout.operator("object.transfer_weights", text="Transfer Weights")

classes = (
    tool_visibility.TOOL_VISIBILITY_HIDE,
    tool_visibility.TOOL_VISIBILITY_SHOW,
    tool_weight_transfer.WEIGHT_OT_transfer_weights,
    TOOLS_PT_LEIDO_Panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)