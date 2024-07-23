# window.py
#
# Copyright 2024 Unknown
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

from gi.repository import Adw, Gio, Gtk

@Gtk.Template(resource_path='/com/ismailarilik/Pickaxe/window.ui')
class PickaxeWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PickaxeWindow'

    editor_view = Gtk.Template.Child()
    open_file_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        open_file_action = Gio.SimpleAction(name='open_file')
        open_file_action.connect('activate', self.open_file_dialog)
        self.add_action(open_file_action)

    def open_file_dialog(self, action, _):
        # Create a new file selection dialog, using the "open" mode
        native = Gtk.FileDialog()
        native.open(self, None, self.on_open_file_response)

    def on_open_file_response(self, dialog, result):
        file = dialog.open_finish(result)
        # If the user selected a file...
        if file is not None:
            # ... open it
            self.open_file(file)

    def open_file(self, file):
        file.load_contents_async(None, self.open_file_complete)

    def open_file_complete(self, file, result):
        info = file.query_info(
            'standard::display-name',
            Gio.FileQueryInfoFlags.NONE
        )
        if info:
            display_name = info.get_attribute_string('standard::display-name')
        else:
            display_name = file.get_basename()

        contents = file.load_contents_finish(result)
        if not contents[0]:
            path = file.peek_path()
            print(f'Unable to open {path}: {contents[1]}')

        try:
            text = contents[1].decode('utf-8')
        except UnicodeError as err:
            path = file.peek_path()
            print(
                f'Unable to load the contents of {path}: '
                'the file is not encoded with UTF-8'
            )
            return

        buffer = self.editor_view.get_buffer()
        buffer.set_text(text)
        start = buffer.get_start_iter()
        buffer.place_cursor(start)

        self.set_title(display_name)
