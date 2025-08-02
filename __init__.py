# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



# ----------------------------------------------
# Import modules
# ----------------------------------------------

if "bpy" in locals():
    import importlib

    importlib.reload(papers)
else:
    from . import papers

import bpy


##############################################################################
# Add-On Handling
##############################################################################
__classes__ = (
    papers.OBJECT_OT_add_paper_mesh,
)


def menu_func(self, context):
    self.layout.operator(
        papers.OBJECT_OT_add_paper_mesh.bl_idname,
        text="Add Std Paper Format",
        icon='CON_SIZELIMIT')


def register():
    # register classes
    for cls in __classes__:
        bpy.utils.register_class(cls)
        print(f'registered {cls}')
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    # unregister classes
    for cls in __classes__:
        bpy.utils.unregister_class(cls)
        print(f'unregistered {cls}')
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)



if __name__ == "__main__":
    register()