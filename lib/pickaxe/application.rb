# frozen_string_literal: true

require_relative 'ui/window'

module Pickaxe
  # Application class
  class Application
    def initialize
      @window = Window.new
    end

    def start
      @window.run
    end
  end
end
