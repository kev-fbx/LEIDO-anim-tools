import bpy

class WEIGHT_OT_transfer_weights(bpy.types.Operator):
    """Transfer vertex weights between meshes"""
    bl_idname = "object.transfer_weights"
    bl_label = "Transfer Vertex Weights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.weight_paint_toggle()
        bpy.ops.object.data_transfer(
            use_reverse_transfer=True,
            data_type='VGROUP_WEIGHTS',
            vert_mapping='POLYINTERP_NEAREST',
            layers_select_src='NAME',
            layers_select_dst='ALL'
        )
        bpy.ops.paint.weight_paint_toggle()
        return {'FINISHED'}
