# frozen_string_literal: true

RSpec.describe Pickaxe::Application do
  let(:application) { described_class.new }

  it 'sets title to "pickaxe"' do
    expect(application.title).to eq('pickaxe')
  end
end
