# main.py
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

import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, GLib
from .window import PickaxeWindow

class PickaxeApplication(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id="com.ismailarilik.Pickaxe", flags=Gio.ApplicationFlags.DEFAULT_FLAGS)

        self.settings = Gio.Settings(schema_id="com.ismailarilik.Pickaxe")

        self.set_initial_color_scheme()

        self.add_actions()

        self.set_accels()

    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if necessary.
        """
        win = self.props.active_window
        if not win:
            win = PickaxeWindow(application=self)
        win.present()

    def set_initial_color_scheme(self):
        dark_mode = self.settings.get_boolean("dark-mode")
        style_manager = Adw.StyleManager.get_default()
        if dark_mode:
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
        else:
            style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)

    def add_actions(self):
        dark_mode = self.settings.get_boolean("dark-mode")
        dark_mode_action = Gio.SimpleAction(name="dark-mode", state=GLib.Variant.new_boolean(dark_mode))
        dark_mode_action.connect("activate", self.toggle_dark_mode)
        dark_mode_action.connect("change-state", self.change_color_scheme)
        self.add_action(dark_mode_action)

        self.create_action("quit", lambda *__: self.quit(), ["<primary>q"])
        self.create_action("about", self.on_about_action)
        self.create_action("preferences", self.on_preferences_action)

    def set_accels(self):
        self.set_accels_for_action("win.open-file", ["<Ctrl>o"])
        self.set_accels_for_action("win.save", ["<Ctrl>s"])
        self.set_accels_for_action("win.save-as", ["<Ctrl><Shift>s"])

    def toggle_dark_mode(self, action, __):
        state = action.get_state()
        old_state = state.get_boolean()
        new_state = not old_state
        action.change_state(GLib.Variant.new_boolean(new_state))

    def change_color_scheme(self, action, new_state):
        dark_mode = new_state.get_boolean()
        style_manager = Adw.StyleManager.get_default()
        if dark_mode:
            style_manager.set_color_scheme(Adw.ColorScheme.FORCE_DARK)
        else:
            style_manager.set_color_scheme(Adw.ColorScheme.DEFAULT)
        action.set_state(new_state)
        self.settings.set_boolean("dark-mode", dark_mode)

    def on_about_action(self, widget, __):
        """Callback for the app.about action."""
        about = Adw.AboutWindow(
            transient_for=self.props.active_window,
            application_name="pickaxe",
            application_icon="com.ismailarilik.Pickaxe",
            developer_name="ismailarilik",
            version="0.1.0",
            developers=["ismailarilik"],
            copyright="© 2024 ismailarilik"
        )
        about.present()

    def on_preferences_action(self, widget, __):
        """Callback for the app.preferences action."""
        print("app.preferences action activated")

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

def main(version):
    """The application's entry point."""
    app = PickaxeApplication()
    return app.run(sys.argv)
