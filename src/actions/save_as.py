# save_as.py
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
from gi.repository import Adw, Gio, GLib, Gtk

_ = gettext.gettext

class SaveAs:
    def __init__(self, window):
        self.window = window

    def save_file_as_dialog(self, action, __):
        native = Gtk.FileDialog()
        native.save(self.window, None, self.on_save_as_response)

    def on_save_as_response(self, dialog, result):
        file = dialog.save_finish(result)
        if file is not None:
            self.save_file(file)

    def save_file(self, file):
        buffer = self.window.editor_view.get_buffer()

        # Retrieve the iterator at the start of the buffer
        start = buffer.get_start_iter()
        # Retrieve the iterator at the end of the buffer
        end = buffer.get_end_iter()
        # Retrieve all the visible text between the two bounds
        text = buffer.get_text(start, end, False)

        # If there is nothing to save, return early
        if not text:
            return

        bytes = GLib.Bytes.new(text.encode("utf-8"))

        # Start the asynchronous operation to save the data into the file
        file.replace_contents_bytes_async(bytes, None, False, Gio.FileCreateFlags.NONE, None, self.save_file_complete)

    def save_file_complete(self, file, result):
        res = file.replace_contents_finish(result)
        info = file.query_info("standard::display-name", Gio.FileQueryInfoFlags.NONE)
        if info:
            display_name = info.get_attribute_string("standard::display-name")
        else:
            display_name = file.get_basename()

        if not res:
            msg = _(f"Unable to save as “{display_name}”")
        else:
            msg = _(f"Saved as “{display_name}”")
            self.window.set_title(display_name)
        self.window.toast_overlay.add_toast(Adw.Toast(title=msg))
