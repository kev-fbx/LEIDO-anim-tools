import bpy

class TOOL_VISIBILITY_HIDE(bpy.types.Operator):
    """Hide and keyframe the render visibility of selected objects"""
    bl_idname = "object.hide_render_visbility"
    bl_label = "Hide and keyframe selected objects render visibility"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            obj.hide_render = True
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}
    
class TOOL_VISIBILITY_UNHIDE(bpy.types.Operator):
    """Show and keyframe the render visibility of selected objects"""
    bl_idname = "object.show_render_visbility"
    bl_label = "Show and keyframe selected objects render visibility"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            obj.hide_render = False
            obj.keyframe_insert(data_path="hide_render")
        return {'FINISHED'}