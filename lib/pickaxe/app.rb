# frozen_string_literal: true

require_relative 'widgets/window'

module Pickaxe
  # The class for the application
  class App
    def initialize
      @window = Widgets::Window.new
    end
  end
end

