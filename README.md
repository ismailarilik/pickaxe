# Pickaxe

> An editor written in Ruby/Tk

Welcome to your new gem! In this directory, you'll find the files you need to be able to package up your Ruby library into a gem. Put your Ruby code in the file `lib/pickaxe`. To experiment with that code, run `bin/console` for an interactive prompt.

## Installation

At first you need to install [Ruby](https://www.ruby-lang.org/) and [Tcl/Tk](https://www.tcl-lang.org/).

Install the gem and add to the application's Gemfile by executing:

```bash
bundle add pickaxe
```

If bundler is not being used to manage dependencies, install the gem by executing:

```bash
gem install pickaxe
```

## Usage

Run the application from the console:

```bash
pickaxe
```

## Development

After checking out the repo, run `bin/setup` to install dependencies. Then, run `rake spec` to run the tests. You can also run `bin/console` for an interactive prompt that will allow you to experiment.

To install this gem onto your local machine, run `bundle exec rake install`. To release a new version, update the version number in `version.rb`, and then run `bundle exec rake release`, which will create a git tag for the version, push git commits and the created tag, and push the `.gem` file to [rubygems.org](https://rubygems.org).

### Checklist

BDD is used for development of this project. For any contribution please follow this path:

1. Write a spec for your contribution.
2. Add your code contribution.
3. Check if all tests pass: `bundle exec rake spec`
4. Check if Rubocop passes: `bundle exec rake rubocop`
5. Update types.
6. Refactor the code.
7. Install the gem into your system: `bundle exec rake install`
8. Run the application from the console: `pickaxe`
9. Update the version number in `version.rb`.
10. Update CHANGELOG.
11. Create the checksum file for this new version: `bundle exec rake build:checksum`
12. Push changes to GitHub.
13. Push the gem to rubygems.org: `bundle exec rake release`

## Contributing

Bug reports and pull requests are welcome on GitHub at [https://github.com/ismailarilik/pickaxe](https://github.com/ismailarilik/pickaxe). This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [code of conduct](https://github.com/ismailarilik/pickaxe/blob/main/CODE_OF_CONDUCT.md).

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the Pickaxe project's codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/ismailarilik/pickaxe/blob/main/CODE_OF_CONDUCT.md).
