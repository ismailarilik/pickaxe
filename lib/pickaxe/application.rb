# frozen_string_literal: true

require 'tk'

module Pickaxe
  # Application class
  class Application
    def initialize
      @window = TkRoot.new
    end

    def start
      @window.mainloop
    end
  end
end
