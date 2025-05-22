import bpy

class VISIBILITY_OT_keyframe_visibility_hide(bpy.types.Operator):
    """Hide and keyframe the render visibility of selected objects"""
    bl_idname = "view3d.keyframe_visibility_hide"
    bl_label = "Hide selected in render"
    bl_info = "Hides selected objects in render and keyframes the change"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = True
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

class VISIBILITY_OT_keyframe_visibility_show(bpy.types.Operator):
    """Show and keyframe the render visibility of selected objects"""
    bl_idname = "view3d.keyframe_visibility_show"
    bl_label = "Show selected in render"
    bl_info = "Shows selected objects in render and keyframes the change"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in bpy.context.selected_objects:
            obj.hide_render = False
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}

# class VISIBILITY_PT_keyframe_visibility_ui(bpy.types.Panel):
#     """UI Panel for visibility keyframing"""
#     bl_label = "Visibility Keyframer"
#     bl_idname = "VISIBILITY_PT_Visibility_Keyframer"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "Animation"

#     def draw(self, context):
#         layout = self.layout
#         scene = context.scene
#         row = layout.row()

#         row = layout.row(align=True)
#         layout.operator("view3d.keyframe_visibility_show", text="Show in render")
#         layout.operator("view3d.keyframe_visibility_hide", text="Hide in render")