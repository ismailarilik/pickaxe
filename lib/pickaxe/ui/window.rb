# frozen_string_literal: true

require 'tk'

module Pickaxe
  # Window class
  class Window
    def initialize
      @tk_window = TkRoot.new
    end

    def run
      @tk_window.mainloop
    end
  end
end
