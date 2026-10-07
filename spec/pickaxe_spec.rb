# frozen_string_literal: true

RSpec.describe Pickaxe do
  it 'has a version number' do
    expect(Pickaxe::VERSION).not_to be_nil
  end

  it 'does something useful' do
    expect(0 < 1).to be(false)
  end
end
