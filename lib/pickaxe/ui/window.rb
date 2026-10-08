# frozen_string_literal: true

require 'tk'

module Pickaxe
  module UI
    # Window class
    class Window
      def initialize
        @tk_window = TkRoot.new
      end

      def title
        @tk_window.title
      end

      def title=(value)
        @tk_window.title = value
      end

      def run
        @tk_window.mainloop
      end
    end
  end
end
