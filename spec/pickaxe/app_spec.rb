# frozen_string_literal: true

RSpec.describe Pickaxe::App do
  it 'initializes a Window object' do
    window = class_spy(Pickaxe::Widgets::Window)
    stub_const('Pickaxe::Widgets::Window', window)

    described_class.new

    expect(window).to have_received(:new).with(no_args)
  end
end

