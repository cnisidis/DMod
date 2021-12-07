import bpy

class DMOD_PT_SETTINGS(bpy.types.Panel):
    bl_label = "DMOD Canvas"
    bl_idname = "DMOD_PT_Settings"
    bl_category = "vvvv | VL"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    def draw(self, context):

        scene = context.scene
        
        layout = self.layout
        row = layout.row()
        row.operator("dmod.udp", text = "START")
        row = layout.row()
        subrow = layout.row(align=True)
        subrow.prop(context.scene.dModSettings, 'bool_start_receiving', text="",  icon="PLAY")
        
        #row.label(text="DMod Canvas UDP Server")
        

class DMOD_Settings(bpy.types.PropertyGroup):
    bool_start_receiving    : bpy.props.BoolProperty(name='Start Sharing', default=False)   
    bool_stop_receiving     : bpy.props.BoolProperty(name='Stop Sharing', default=False)