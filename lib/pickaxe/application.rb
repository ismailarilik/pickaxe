# frozen_string_literal: true

require_relative 'ui/window'

module Pickaxe
  # Application class
  class Application
    def initialize
      @window = UI::Window.new
      @window.title = 'pickaxe'
    end

    def title
      @window.title
    end

    def start
      @window.run
    end
  end
end
