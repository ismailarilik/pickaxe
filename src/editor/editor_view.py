# editor_view.py
#
# Copyright 2024 ismailarilik
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gio, Gtk

@Gtk.Template(resource_path="/com/ismailarilik/Pickaxe/editor/editor_view.ui")
class EditorView(Gtk.TextView):
    __gtype_name__ = "EditorView"

    def __init__(self, file=None, **kwargs):
        super().__init__(**kwargs)
        self.file = None

    def set_file(self, file):
        self.file = file

        info = self.file.query_info("standard::display-name", Gio.FileQueryInfoFlags.NONE)
        if info:
            display_name = info.get_attribute_string("standard::display-name")
        else:
            display_name = file.get_basename()
        self.display_name = display_name
