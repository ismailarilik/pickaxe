pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'pickaxe'
actionsdir = moduledir / 'actions'
editordir = moduledir / 'editor'
gnome = import('gnome')

gnome.compile_resources(
  'pickaxe',
  'pickaxe.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'pickaxe.in',
  output: 'pickaxe',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr-xr-x'
)

pickaxe_sources = [
  '__init__.py',
  'main.py',
  'window.py',
]
actions_sources = [
  'actions/__init__.py',
  'actions/open_file.py',
  'actions/save.py',
  'actions/save_as.py',
]
editor_sources = [
  'editor/__init__.py',
  'editor/editor_view.py',
]

install_data(pickaxe_sources, install_dir: moduledir)
install_data(actions_sources, install_dir: actionsdir)
install_data(editor_sources, install_dir: editordir)
