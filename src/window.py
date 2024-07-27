# window.py
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

from .actions.open_file import OpenFile
from .actions.save_as import SaveAs
import gettext
from gi.repository import Adw, Gio, Gtk
from .editor.editor_view import EditorView

_ = gettext.gettext

@Gtk.Template(resource_path="/com/ismailarilik/Pickaxe/window.ui")
class PickaxeWindow(Adw.ApplicationWindow):
    __gtype_name__ = "PickaxeWindow"

    cursor_pos: Gtk.Label = Gtk.Template.Child()
    editor_view: EditorView = Gtk.Template.Child()
    menu_button: Gtk.MenuButton = Gtk.Template.Child()
    open_file_button: Gtk.Button = Gtk.Template.Child()
    toast_overlay: Adw.ToastOverlay = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app_name = "Pickaxe"
        self.open_file = OpenFile(self)
        self.save_as = SaveAs(self)

        menu_builder = Gtk.Builder.new_from_resource("/com/ismailarilik/Pickaxe/menu.ui")
        primary_menu = menu_builder.get_object("primary_menu")
        self.menu_button.set_menu_model(primary_menu)

        self.add_actions()

        buffer = self.editor_view.get_buffer()
        buffer.connect("notify::cursor-position", self.update_cursor_position)

        self.set_initial_settings()

    def add_actions(self):
        self.create_action("open-file", self.open_file.open_file_dialog)
        self.create_action("save-as", self.save_as.save_file_as_dialog)

    def update_cursor_position(self, buffer, __):
        # Retrieve the value of the "cursor-position" property
        cursor_pos = buffer.props.cursor_position
        # Construct the text iterator for the position of the cursor
        iter = buffer.get_iter_at_offset(cursor_pos)
        line = iter.get_line() + 1
        column = iter.get_line_offset() + 1
        # Set the new contents of the label
        self.cursor_pos.set_text(_(f"Ln {line}, Col {column}"))

    def create_action(self, name, callback, accels=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is activated
            accels: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name)
        action.connect("activate", callback)
        self.add_action(action)
        if accels:
            self.set_accels_for_action(f"app.{name}", accels)

    def set_initial_settings(self):
        self.settings = Gio.Settings(schema_id="com.ismailarilik.Pickaxe")
        self.settings.bind("window-width", self, "default-width", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("window-height", self, "default-height", Gio.SettingsBindFlags.DEFAULT)
        self.settings.bind("window-maximized", self, "maximized", Gio.SettingsBindFlags.DEFAULT)
