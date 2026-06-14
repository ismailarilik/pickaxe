require 'tk'
require_relative 'editor/notebook'
require_relative 'explorer/treeview'

module Pickaxe
  class ApplicationWindow < Tk::Root
    def initialize(...)
      super

      self.title = 'Pickaxe'

      # Set icon
      icon_path = File.join __dir__, 'pickaxe.png'
      icon = TkPhotoImage.new file: icon_path
      self.iconphoto = icon

      pack_widgets

      bind_keys
      bind_protocols

      resize_and_center
    end

    def pack_widgets
      paned_view = Ttk::Paned.new self, orient: :horizontal
      paned_view.pack fill: :both, expand: true

      @explorer_tree_view = Explorer::Treeview.new paned_view, method(:on_file_double_clicked_on_explorer_tree_view)
      paned_view.add @explorer_tree_view

      @editor_notebook = Editor::Notebook.new paned_view
      paned_view.add @editor_notebook
    end

    def bind_keys
      bind 'Control-n', method(:on_control_n)
      bind 'Control-N', method(:on_control_n)
      bind 'Control-o', method(:on_control_o)
      bind 'Control-O', method(:on_control_o)
      bind 'Control-Shift-o', method(:on_control_shift_o)
      bind 'Control-Shift-O', method(:on_control_shift_o)
      bind 'Control-s', method(:on_control_s)
      bind 'Control-S', method(:on_control_s)
      bind 'Control-Shift-s', method(:on_control_shift_s)
      bind 'Control-Shift-S', method(:on_control_shift_s)
      bind 'Control-q', method(:on_control_q)
      bind 'Control-Q', method(:on_control_q)
    end

    def bind_protocols
      protocol 'WM_DELETE_WINDOW', method(:on_wm_delete_window)
    end

    def resize_and_center
      screen_width = winfo_screenwidth
      screen_height = winfo_screenheight
      width = screen_width / 2
      height = screen_height / 2
      x = (screen_width / 2) - (width / 2)
      y = (screen_height / 2) - (height / 2)
      geometry("#{width}x#{height}+#{x}+#{y}")
    end

    def open_file(file_path)
      @editor_notebook.add_code_view file_path if file_path
    end

    def ask_for_unsaved_changes
      title = 'Unsaved Changes'
      message = 'There are unsaved changes'
      detail = 'Do you want to save?'
      ask_result = Tk.messageBox(
        type: :yesnocancel,
        default: :yes,
        icon: :warning,
        title: title,
        message: message,
        detail: detail
      )
      final_result = false
      final_result = false if ask_result == 'cancel'
      final_result = true if ask_result == 'no'
      if ask_result == 'yes'
        final_result = save_unsaved_changes
      end
      final_result
    end

    def has_unsaved_changes?
      @editor_notebook.has_unsaved_changes?
    end

    def save_unsaved_changes
      @editor_notebook.save_unsaved_changes
    end

    def save_file_as
      @editor_notebook.save_current_code_view_as
    end

    def quit
      will_be_destroyed = true
      will_be_destroyed = ask_for_unsaved_changes if has_unsaved_changes?
      destroy if will_be_destroyed
    end

    def on_control_n
      @editor_notebook.add_code_view
    end

    def on_control_o
      file_path = Tk.getOpenFile
      unless file_path.empty?
        open_file file_path
      end
    end

    def on_control_shift_o
      folder_path = Tk.chooseDirectory
      unless folder_path.empty?
        @explorer_tree_view.open_folder folder_path
      end
    end

    def on_control_s
      saved = @editor_notebook.save_current_code_view

      unless saved
        save_file_as
      end
    end

    def on_control_shift_s
      save_file_as
    end

    def on_control_q
      quit
    end

    def on_wm_delete_window
      quit
    end

    def on_file_double_clicked_on_explorer_tree_view(event, file_path)
      open_file file_path
    end
  end
end
