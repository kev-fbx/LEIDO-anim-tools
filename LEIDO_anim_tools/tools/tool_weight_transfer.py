import bpy

class transfer_weights(bpy.types.Operator):
    """Transfer vertex weights between meshes"""
    bl_label = "Transfer weights"
    bl_idname = "view3d.transfer_weights"
    bl_info = "Transfers vertex weights between meshes"
    bl_options = {'REGISTER', 'UNDO'}
    
    # Operation to transfer weights
    def execute(self, context):
        bpy.ops.paint.weight_paint_toggle()
        bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', vert_mapping='POLYINTERP_NEAREST', layers_select_src='NAME', layers_select_dst='ALL')
        bpy.ops.paint.weight_paint_toggle()
        return {"FINISHED"}

# class WEIGHT_TRANSFER_PT_ui(bpy.types.Panel):
#     """UI panel for weight transfer"""
#     bl_label = "Weight Transfer"
#     bl_idname = "VIEW3D_PT_Weight_Transfer"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = "Tool"

#     def draw(self, context):
#         """Define the layout of the panel"""
#         layout = self.layout
#         scene = context.scene
#         row = layout.row()
        
#         row = layout.row(align=True)
#         layout.operator("view3d.transfer_weights")