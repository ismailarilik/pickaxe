import unittest
from unittest.mock import Mock
import gettext
import gi.repository
gi.repository.Adw = Mock()
gi.repository.Gio = Mock()
gi.repository.GLib = Mock()
gi.repository.Gtk = Mock()
from src.actions.save import Save

class TestSaveAction(unittest.TestCase):
    def setUp(self):
        gettext.gettext = Mock(side_effect=lambda string: string)
        self.window = Mock()
        self.save_action = Save(self.window)

    # Test if the function `save_file` is called with the value `self.window.editor_view.file`
    # after calling the function `save_file_or_save_file_as_dialog`
    # when `self.window.editor_view.file` is defined.
    def test_save_file_is_called_with_file_after_calling_save_file_or_save_file_as_dialog_when_file_is_defined(self):
        self.window.editor_view.file = Mock()
        self.save_action.save_file = Mock()
        self.save_action.save_file_or_save_file_as_dialog(None, None)
        self.save_action.save_file.assert_called_with(self.window.editor_view.file)

    # Test if the function `save_file_dialog` is called
    # after calling the function `save_file_or_save_file_as_dialog`
    # when `self.window.editor_view.file` is not defined.
    def test_save_file_dialog_is_called_after_calling_save_file_or_save_file_as_dialog_when_file_is_not_defined(self):
        self.window.editor_view.file = None
        self.save_action.save_file_dialog = Mock()
        self.save_action.save_file_or_save_file_as_dialog(None, None)
        self.save_action.save_file_dialog.assert_called_once()

    # Test if the property `is_file_saved_as_another_name` is set to `False`
    # after calling the function `save_file_or_save_file_as_dialog`
    # when `self.window.editor_view.file` is defined.
    def test_is_file_saved_as_another_name_is_false_after_calling_save_file_or_save_file_as_dialog_when_file_is_defined(self):
        self.window.editor_view.file = Mock()
        self.save_action.save_file_or_save_file_as_dialog(None, None)
        self.assertFalse(self.save_action.is_file_saved_as_another_name)

    # Test if the property `is_file_saved_as_another_name` is set to `True`
    # after calling the function `save_file_or_save_file_as_dialog`
    # when `self.window.editor_view.file` is not defined.
    def test_is_file_saved_as_another_name_is_true_after_calling_save_file_or_save_file_as_dialog_when_file_is_not_defined(self):
        self.window.editor_view.file = None
        self.save_action.save_file_or_save_file_as_dialog(None, None)
        self.assertTrue(self.save_action.is_file_saved_as_another_name)
