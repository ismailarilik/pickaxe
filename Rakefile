# frozen_string_literal: true

require 'bundler/gem_tasks'
require 'rspec/core/rake_task'

RSpec::Core::RakeTask.new(:spec)

require 'rubocop/rake_task'

RuboCop::RakeTask.new

ENV['RBS_TEST_LOGLEVEL'] = 'error'
ENV['RBS_TEST_TARGET'] = 'Pickaxe::*'
ENV['RBS_TEST_RAISE'] = 'true'
ENV['RUBYOPT'] = '-rbundler/setup -rrbs/test/setup'

task default: %i[spec rubocop]

