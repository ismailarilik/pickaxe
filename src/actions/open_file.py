# open_file.py
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

import gettext
from gi.repository import Adw, Gio, Gtk

_ = gettext.gettext

class OpenFile:
    def __init__(self, window):
        self.window = window
        self.editor_view = self.window.editor_view

    def open_file_dialog(self, action, __):
        # Create a new file selection dialog, using the "open" mode
        native = Gtk.FileDialog()
        native.open(self.window, None, self.on_open_file_response)

    def on_open_file_response(self, dialog, result):
        file = dialog.open_finish(result)
        # If the user selected a file...
        if file is not None:
            # ... open it
            self.open_file(file)

    def open_file(self, file):
        file.load_contents_async(None, self.open_file_complete)

    def open_file_complete(self, file, result):
        info = file.query_info("standard::display-name", Gio.FileQueryInfoFlags.NONE)
        if info:
            display_name = info.get_attribute_string("standard::display-name")
        else:
            display_name = file.get_basename()

        contents = file.load_contents_finish(result)
        if not contents[0]:
            self.window.toast_overlay.add_toast(Adw.Toast(title=_(f"Unable to open “{display_name}”")))
            return

        try:
            text = contents[1].decode("utf-8")
        except UnicodeError as err:
            self.window.toast_overlay.add_toast(Adw.Toast(title=_(f"Invalid text encoding for “{display_name}”")))
            return

        buffer = self.editor_view.get_buffer()
        buffer.set_text(text)

        start = buffer.get_start_iter()
        buffer.place_cursor(start)

        self.editor_view.set_file(file)
        self.window.set_title(f"{self.editor_view.display_name} - {self.window.app_name}")
