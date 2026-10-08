# frozen_string_literal: true

RSpec.describe Pickaxe::UI::Window do
  let(:window) { described_class.new }

  it 'sets title correctly' do
    window.title = 'Test'
    expect(window.title).to eq('Test')
  end
end
