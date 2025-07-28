# GPL-3.0 license

import bpy



PAPER_STANDARDS = {
    'ISO_A': [
        ('A0', 'A0', '', 841, 1189),
        ('A1', 'A1', '', 594, 841),
        ('A2', 'A2', '', 420, 594),
        ('A3', 'A3', '', 297, 420),
        ('A4', 'A4', '', 210, 297),
        ('A5', 'A5', '', 148, 210),
        ('A6', 'A6', '', 105, 148),
        ('A7', 'A7', '', 74, 105),
        ('A8', 'A8', '', 52, 74),
        ('A9', 'A9', '', 37, 52),
        ('A10', 'A10', '', 26, 37),
        ('A11', 'A11', '', 18, 26),
        ('A12', 'A12', '', 13, 18),
        ('A13', 'A13', '', 9, 13),
        ('2A0', '2A0', '', 1189, 1682),
        ('4A0', '4A0', '', 1682, 2378),
        ('A0+', 'A0+', '', 914, 1292),
        ('A1+', 'A1+', '', 609, 914),
        ('A3+', 'A3+', '', 329, 483)
    ],
    'ISO_B': [
        ('B0', 'B0', '', 1000, 1414),
        ('B1', 'B1', '', 707, 1000),
        ('B2', 'B2', '', 500, 707),
        ('B3', 'B3', '', 353, 500),
        ('B4', 'B4', '', 250, 353),
        ('B5', 'B5', '', 176, 250),
        ('B6', 'B6', '', 125, 176),
        ('B7', 'B7', '', 88, 125),
        ('B8', 'B8', '', 62, 88),
        ('B9', 'B9', '', 44, 62),
        ('B10', 'B10', '', 31, 44),
        ('B11', 'B11', '', 22, 31),
        ('B12', 'B12', '', 15, 22),
        ('B13', 'B13', '', 11, 15),
        ('B0+', 'B0+', '', 1118, 1580),
        ('B1+', 'B1+', '', 720, 1020),
        ('B2+', 'B2+', '', 520, 720)
    ],
    'ISO_C': [
        ('C0', 'C0', '', 917, 1297),
        ('C1', 'C1', '', 648, 917),
        ('C2', 'C2', '', 458, 648),
        ('C3', 'C3', '', 324, 458),
        ('C4', 'C4', '', 229, 324),
        ('C5', 'C5', '', 162, 229),
        ('C6', 'C6', '', 114, 162),
        ('C7', 'C7', '', 81, 114),
        ('C8', 'C8', '', 57, 81),
        ('C9', 'C9', '', 40, 57),
        ('C10', 'C10', '', 28, 40)
    ],
    'US_Paper': [
        ('Letter', 'Letter', '', 216, 279),
        ('Legal', 'Legal', '', 216, 356),
        ('Tabloid', 'Tabloid', '', 279, 432),
        ('Ledger', 'Ledger', '', 432, 279),
        ('Junior Legal', 'Junior Legal', '', 127, 203),
        ('Half Letter', 'Half Letter', '', 140, 216),
        ('Government Letter', 'Government Letter', '', 203, 267),
        ('Government Legal', 'Government Legal', '', 216, 330),
        ('ANSI A', 'ANSI A', '', 216, 279),
        ('ANSI B', 'ANSI B', '', 279, 432),
        ('ANSI C', 'ANSI C', '', 432, 559),
        ('ANSI D', 'ANSI D', '', 559, 864),
        ('ANSI E', 'ANSI E', '', 864, 1118),
        ('Arch A', 'Arch A', '', 229, 305),
        ('Arch B', 'Arch B', '', 305, 457),
        ('Arch C', 'Arch C', '', 457, 610),
        ('Arch D', 'Arch D', '', 610, 914),
        ('Arch E', 'Arch E', '', 914, 1219),
        ('Arch E1', 'Arch E1', '', 762, 1067),
        ('Arch E2', 'Arch E2', '', 660, 965),
        ('Arch E3', 'Arch E3', '', 686, 991)
    ],
    'US_Envelope': [
        ('6¼', '6¼', '', 152, 89),
        ('6¾', '6¾', '', 165, 92),
        ('7', '7', '', 172, 95),
        ('7¾ Monarch', '7¾ Monarch', '', 191, 98),
        ('8⅝', '8⅝', '', 219, 92),
        ('9', '9', '', 225, 98),
        ('10', '10', '', 241, 104),
        ('11', '11', '', 264, 114),
        ('12', '12', '', 279, 121),
        ('14', '14', '', 292, 127),
        ('16', '16', '', 305, 152),
        ('A1', 'A1', '', 92, 130),
        ('A2 Lady Grey', 'A2 Lady Grey', '', 146, 111),
        ('A4', 'A4', '', 159, 108),
        (u'A6 Thompson\'s Standard', u'A6 Thompson\'s Standard', '', 165, 121),
        ('A7 Besselheim', 'A7 Besselheim', '', 184, 133),
        (u'A8 Carr\'s', u'A8 Carr\'s', '', 206, 140),
        ('A9 Diplomat', 'A9 Diplomat', '', 222, 146),
        ('A10 Willow', 'A10 Willow', '', 241, 152),
        ('A Long', 'A Long', '', 225, 98),
        ('1', '1', '', 229, 152),
        ('1¾', '1¾', '', 241, 152),
        ('3', '3', '', 254, 178),
        ('6', '6', '', 267, 191),
        ('8', '8', '', 286, 210),
        ('9¾', '9¾', '', 286, 222),
        ('10½', '10½', '', 305, 229),
        ('12½', '12½', '', 318, 241),
        ('13½', '13½', '', 330, 254),
        ('14½', '14½', '', 368, 292),
        ('15', '15', '', 381, 254),
        ('15½', '15½', '', 394, 305)
    ],
    'International_Envelope ': [
        ('DL', 'DL', '', 220, 110),
        ('B4', 'B4', '', 353, 250),
        ('B5', 'B5', '', 250, 176),
        ('B6', 'B6', '', 176, 125),
        ('C3', 'C3', '', 458, 324),
        ('C4', 'C4', '', 324, 229),
        ('C5', 'C5', '', 229, 162),
        ('C6/C5', 'C6/C5', '', 229, 114),
        ('C6', 'C6', '', 162, 114),
        ('C7/C6', 'C7/C6', '', 162, 81),
        ('C7', 'C7', '', 114, 81),
        ('E4', 'E4', '', 400, 280)
    ],
    'Canadian_Paper': [
        ('P1', 'P1', '', 560, 860),
        ('P2', 'P2', '', 430, 560),
        ('P3', 'P3', '', 280, 430),
        ('P4', 'P4', '', 215, 280),
        ('P5', 'P5', '', 140, 215),
        ('P6', 'P6', '', 107, 140)
    ],
    'Japanese_Paper': [
        ('JB0', 'JB0', '', 1030, 1456),
        ('JB1', 'JB1', '', 728, 1030),
        ('JB2', 'JB2', '', 515, 728),
        ('JB3', 'JB3', '', 364, 515),
        ('JB4', 'JB4', '', 257, 364),
        ('JB5', 'JB5', '', 182, 257),
        ('JB6', 'JB6', '', 128, 182),
        ('JB7', 'JB7', '', 91, 128),
        ('JB8', 'JB8', '', 64, 91),
        ('JB9', 'JB9', '', 45, 64),
        ('JB10', 'JB10', '', 32, 45),
        ('JB11', 'JB11', '', 22, 32),
        ('JB12', 'JB12', '', 16, 22),
        ('Shiroku ban 4', 'Shiroku ban 4', '', 264, 379),
        ('Shiroku ban 5', 'Shiroku ban 5', '', 189, 262),
        ('Shiroku ban 6', 'Shiroku ban 6', '', 127, 188),
        ('Kiku 4', 'Kiku 4', '', 227, 306),
        ('Kiku 5', 'Kiku 5', '', 151, 227)
    ],
    'Chinese_Paper': [
        ('D0', 'D0', '', 764, 1064),
        ('D1', 'D1', '', 532, 760),
        ('D2', 'D2', '', 380, 528),
        ('D3', 'D3', '', 264, 376),
        ('D4', 'D4', '', 188, 260),
        ('D5', 'D5', '', 130, 184),
        ('D6', 'D6', '', 92, 126),
        ('RD0', 'RD0', '', 787, 1092),
        ('RD1', 'RD1', '', 546, 787),
        ('RD2', 'RD2', '', 393, 546),
        ('RD3', 'RD3', '', 273, 393),
        ('RD4', 'RD4', '', 196, 273),
        ('RD5', 'RD5', '', 136, 196),
        ('RD6', 'RD6', '', 98, 136)
    ],
    'Colombian_Paper': [
        ('Carta', 'Carta', '', 216, 279),
        ('Extra Tabloide', 'Extra Tabloide', '', 304, 457.2),
        ('Oficio', 'Oficio', '', 216, 330),
        ('1/8 pliego', '1/8 pliego', '', 250, 350),
        ('1/4 pliego', '1/4 pliego', '', 350, 500),
        ('1/2 pliego', '1/2 pliego', '', 500, 700),
        ('Pliego', 'Pliego', '', 700, 1000)
    ],
    'Billboard_Paper': [
        ('1 Sheet', '1 Sheet', '', 508, 762),
        ('2 Sheet', '2 Sheet', '', 762, 1016),
        ('4 Sheet', '4 Sheet', '', 1016, 1524),
        ('6 Sheet', '6 Sheet', '', 1200, 1800),
        ('12 Sheet', '12 Sheet', '', 3048, 1524),
        ('16 Sheet', '16 Sheet', '', 2032, 3048),
        ('32 Sheet', '32 Sheet', '', 4064, 3048),
        ('48 Sheet', '48 Sheet', '', 6096, 3048),
        ('64 Sheet', '64 Sheet', '', 8128, 3048),
        ('96 Sheet', '96 Sheet', '', 12192, 3048)
    ],
    'Newspaper': [
        ('Berliner', 'Berliner', '', 315, 470),
        ('Broadsheet', 'Broadsheet', '', 597, 749),
        ('US Broadsheet', 'US Broadsheet', '', 381, 578),
        ('British Broadsheet', 'British Broadsheet', '', 375, 597),
        ('South African Broadsheet', 'South African Broadsheet', '', 410, 578),
        ('Ciner', 'Ciner', '', 350, 500),
        ('Compact', 'Compact', '', 280, 430),
        ('Nordisch', 'Nordisch', '', 400, 570),
        ('Rhenish', 'Rhenish', '', 350, 520),
        ('Swiss', 'Swiss', '', 320, 475),
        ('Tabloid', 'Tabloid', '', 280, 430),
        ('Canadian Tabloid', 'Canadian Tabloid', '', 260, 368),
        ('Norwegian Tabloid', 'Norwegian Tabloid', '', 280, 400),
        ('New York Times', 'New York Times', '', 305, 559),
        ('Wall Street Journal', 'Wall Street Journal', '', 305, 578)
    ],
    'Business_Cards': [
        ('ISO 216', 'ISO 216', '', 74, 52),
        ('US/Canada', 'US/Canada', '', 88.9, 50.8),
        ('European', 'European', '', 85, 55),
        ('Scandinavia', 'Scandinavia', '', 90, 55),
        ('China', 'China', '', 90, 54),
        ('Japan', 'Japan', '', 91, 55),
        ('Iran', 'Iran', '', 85, 48),
        ('ISO 7810 ID-1', 'ISO 7810 ID-1', '', 85.6, 54)
    ],
    'Books': [
        ('Folio', 'Folio', '', 304.8, 482.6),
        ('Quarto', 'Quarto', '', 241.3, 304.8),
        ('Imperial Octavo', 'Imperial Octavo', '', 209.6, 292.1),
        ('Super Octavo', 'Super Octavo', '', 177.8, 279.4),
        ('Royal Octavo', 'Royal Octavo', '', 165.1, 254),
        ('Medium Octavo', 'Medium Octavo', '', 165.1, 234.9),
        ('Octavo', 'Octavo', '', 152.4, 228.6),
        ('Crown Octavo', 'Crown Octavo', '', 136.5, 203.2),
        ('12mo', '12mo', '', 127, 187.3),
        ('16mo', '16mo', '', 101.6, 171.4),
        ('18mo', '18mo', '', 101.6, 165.1),
        ('32mo', '32mo', '', 88.9, 139.7),
        ('48mo', '48mo', '', 63.5, 101.6),
        ('64mo', '64mo', '', 50.8, 76.2),
        ('A Format', 'A Format', '', 110, 178),
        ('B Format', 'B Format', '', 129, 198),
        ('C Format', 'C Format', '', 135, 216)
    ],
    'British_Imperial': [
        ('Antiquarian', 'Antiquarian', '', 787, 1346),
        ('Atlas', 'Atlas', '', 660, 864),
        ('Brief', 'Brief', '', 343, 406),
        ('Broadsheet', 'Broadsheet', '', 457, 610),
        ('Cartridge', 'Cartridge', '', 533, 660),
        ('Columbier', 'Columbier', '', 597, 876),
        ('Copy Draught', 'Copy Draught', '', 406, 508),
        ('Crown', 'Crown', '', 381, 508),
        ('Demy', 'Demy', '', 445, 572),
        ('Double Demy', 'Double Demy', '', 572, 902),
        ('Quad Demy', 'Quad Demy', '', 889, 1143),
        ('Elephant', 'Elephant', '', 584, 711),
        ('Double Elephant', 'Double Elephant', '', 678, 1016),
        ('Emperor', 'Emperor', '', 1219, 1829),
        ('Foolscap', 'Foolscap', '', 343, 432),
        ('Small Foolscap', 'Small Foolscap', '', 337, 419),
        ('Grand Eagle', 'Grand Eagle', '', 730, 1067),
        ('Imperial', 'Imperial', '', 559, 762),
        ('Medium', 'Medium', '', 470, 584),
        ('Monarch', 'Monarch', '', 184, 267),
        ('Post', 'Post', '', 394, 489),
        ('Sheet, Half Post', 'Sheet, Half Post', '', 495, 597),
        ('Pinched Post', 'Pinched Post', '', 375, 470),
        ('Large Post', 'Large Post', '', 394, 508),
        ('Double Large Post', 'Double Large Post', '', 533, 838),
        ('Double Post', 'Double Post', '', 483, 762),
        ('Pott', 'Pott', '', 318, 381),
        ('Princess', 'Princess', '', 546, 711),
        ('Quarto', 'Quarto', '', 229, 279),
        ('Royal', 'Royal', '', 508, 635),
        ('Super Royal', 'Super Royal', '', 483, 686)
    ],
    'Transitional': [
        ('PA0', 'PA0', '', 840, 1120),
        ('PA1', 'PA1', '', 560, 840),
        ('PA2', 'PA2', '', 420, 560),
        ('PA3', 'PA3', '', 280, 420),
        ('PA4', 'PA4', '', 210, 280),
        ('PA5', 'PA5', '', 140, 210),
        ('PA6', 'PA6', '', 105, 140),
        ('PA7', 'PA7', '', 70, 105),
        ('PA8', 'PA8', '', 52, 70),
        ('PA9', 'PA9', '', 35, 52),
        ('PA10', 'PA10', '', 26, 35),
        ('F0', 'F0', '', 841, 1321),
        ('F1', 'F1', '', 660, 841),
        ('F2', 'F2', '', 420, 660),
        ('F3', 'F3', '', 330, 420),
        ('F4', 'F4', '', 210, 330),
        ('F5', 'F5', '', 165, 210),
        ('F6', 'F6', '', 105, 165),
        ('F7', 'F7', '', 82, 105),
        ('F8', 'F8', '', 52, 82),
        ('F9', 'F9', '', 41, 52),
        ('F10', 'F10', '', 26, 41)
    ],
    'Traditional_British': [
        ('Dukes', 'Dukes', '', 140, 178),
        ('Foolscap', 'Foolscap', '', 203, 330),
        ('Imperial', 'Imperial', '', 178, 229),
        ('Kings', 'Kings', '', 165, 203),
        ('Quarto', 'Quarto', '', 203, 254)
    ],
    'RA_and_SRA': [
        ('RA0', 'RA0', '', 860, 1220),
        ('RA1', 'RA1', '', 610, 860),
        ('RA2', 'RA2', '', 430, 610),
        ('RA3', 'RA3', '', 305, 430),
        ('RA4', 'RA4', '', 215, 305),
        ('SRA0', 'SRA0', '', 900, 1280),
        ('SRA1', 'SRA1', '', 640, 900),
        ('SRA2', 'SRA2', '', 450, 640),
        ('SRA3', 'SRA3', '', 320, 450),
        ('SRA4', 'SRA4', '', 225, 320),
        ('SRA1+', 'SRA1+', '', 660, 920),
        ('SRA2+', 'SRA2+', '', 480, 650),
        ('SRA3+', 'SRA3+', '', 320, 460),
        ('SRA3++', 'SRA3++', '', 320, 464),
        ('A0U', 'A0U', '', 880, 1230),
        ('A1U', 'A1U', '', 625, 880),
        ('A2U', 'A2U', '', 450, 625),
        ('A3U', 'A3U', '', 330, 450),
        ('A4U', 'A4U', '', 240, 330)
    ]
}

def get_standard_items(self, context):
    return [(k, k.replace('_', ' '), '') for k in PAPER_STANDARDS.keys()]

def get_format_items(self, context):
    return [(f[0], f[1], f[2]) for f in PAPER_STANDARDS[self.paper_standard]]

def update_standard(self, context):
    # Reset format to first available when standard changes
    self.paper_format = PAPER_STANDARDS[self.paper_standard][0][0]
    update_format(self, context)

def update_format(self, context):
    # Set size_x and size_y based on selected format
    for f in PAPER_STANDARDS[self.paper_standard]:
        if f[0] == self.paper_format:
            self.size_x = f[3] / 1000  # Convert mm to meters
            self.size_y = f[4] / 1000
            break

class OBJECT_OT_add_paper_mesh(bpy.types.Operator):
    bl_idname = "mesh.add_paper_mesh"
    bl_label = "Add Std Paper Format"
    bl_options = {'REGISTER', 'UNDO'}

    flip: bpy.props.BoolProperty(
        name='Flip',
        description='Flip the paper mesh',
        default=False
        )
    uv_ratio: bpy.props.BoolProperty(
        name='Adjust UV-Ratio',
        description='Adjust Aspect Ratio of UVs to match paper size',
        default=True
        )
    size_x: bpy.props.FloatProperty(
        name='Size x',
        default=1,
        soft_min=0,
        soft_max=10,
        subtype='DISTANCE',
        unit='LENGTH',
        precision=4
        )    
    size_y: bpy.props.FloatProperty(
        name='Size y',
        default=1,
        soft_min=0,
        soft_max=10,
        subtype='DISTANCE',
        unit='LENGTH',
        precision=4
        )
    paper_standard: bpy.props.EnumProperty(
        name="Standard",
        description="Paper format standard",
        items=get_standard_items,
        update=update_standard
    )
    paper_format: bpy.props.EnumProperty(
        name="Format",
        description="Paper format size",
        items=get_format_items,
        update=update_format
    )
    str_size_mm: bpy.props.StringProperty(
        name="Size [mm]"
    )
    str_size_in: bpy.props.StringProperty(
        name="Size [in]"
    )
    
    def invoke(self, context, event):
        # set default object types:

        self.size_x = 1
        self.size_y = 1

        self.paper_standard = 'ISO_A'
        self.paper_format = 'A4'
        update_format(self, context)

        return self.execute(context)

    def execute(self, context):
        #self.new_plane.scale = (self.size_x, self.size_y, 1)
        #self.report({'INFO'}, 'exec')

        if self.flip:
            SH = self.size_y
            SV = self.size_x
        else:
            SH = self.size_x
            SV = self.size_y
        
        self.str_size_mm = '{:.1f}x{:.1f} mm'.format(SH*1000, SV*1000)
        self.str_size_in = '{:.1f}x{:.1f} in'.format(SH*1000/25.4, SV*1000/25.4)

        bpy.ops.mesh.primitive_plane_add(size=1)
        bpy.ops.transform.resize(value=(SH, SV, 1))
        bpy.ops.object.transform_apply(scale=True)

        bpy.context.active_object.name = "PaperMesh_{}_{}".format(self.paper_standard, self.paper_format)
        bpy.context.active_object.data.name = "PaperMesh_{}_{}".format(self.paper_standard, self.paper_format)
        
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        if self.uv_ratio:
            bpy.ops.uv.cube_project(correct_aspect=True)
        else:
            bpy.ops.uv.cube_project(correct_aspect=False,scale_to_bounds=True)
        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
    
        layout.use_property_split = True
        
        box = layout.box()
        box.label(text='Paper Standard & Format', icon='GESTURE_ZOOM')
        box.prop(self, 'paper_standard')
        box.prop(self, 'paper_format')
        box.prop(self, 'flip', toggle=False, icon='FILE_REFRESH')
        box.prop(self, 'uv_ratio', toggle=True, icon='UV_FACESEL')

        layout.separator(factor=1)
                
        box = layout.box()
        box.label(text='Dimensions', icon='FIXED_SIZE')
        
        row = box.row()
        box.prop(self, 'size_x', slider=True)
        box.prop(self, 'size_y', slider=True)
        
        row = box.row()
        split = row.split(factor=0.5)
        split.label(text=self.str_size_mm)
        split_right = split.split(factor=1.0)
        split_right.alignment = 'RIGHT'
        split_right.label(text=self.str_size_in)

        

def menu_func(self, context):
    self.layout.operator(
        OBJECT_OT_add_paper_mesh.bl_idname,
        text="Add Std Paper Format",
        icon='CON_SIZELIMIT')

     #self.layout.operator("mesh.add_paper_mesh", icon='CON_SIZELIMIT')




##############################################################################
# Add-On Handling
##############################################################################
__classes__ = (
    OBJECT_OT_add_paper_mesh,
)


def register():
    # register classes
    for c in __classes__:
        bpy.utils.register_class(c)
        print(f'registered {c}')
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    # unregister classes
    for c in __classes__:
        bpy.utils.unregister_class(c)
        print(f'unregistered {c}')
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)
