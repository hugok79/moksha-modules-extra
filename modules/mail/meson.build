#### Project ####
project('mail', 'c',
        version: '0.1.1',
        meson_version: '>= 0.58.0')

add_project_arguments('-D__UNUSED__=__attribute__((unused))', language: 'c')

gettext_domain = 'e-module-' + meson.project_name()

### Checks for library functions.
cc = meson.get_compiler('c')

if not cc.has_function('strdup')
  error('The required function strdup() is not available.')
endif

#### Enlightenment ####
dep_e = dependency('enlightenment')
e_modules_dir = dep_e.get_variable('modules')
e_module_arch = dep_e.get_variable('module_arch')

#### Install dirs ####
dir_prefix      = get_option('prefix')
mod_install_dir = join_paths(e_modules_dir, meson.project_name())
lib_install_dir = join_paths(mod_install_dir, e_module_arch)
data_dir        = join_paths(dir_prefix, get_option('datadir'))
mod_data_dir    = join_paths(data_dir, meson.project_name())

#### config.h ####
config_h = configuration_data()
config_h.set_quoted('PACKAGE', meson.project_name())
config_h.set_quoted('LOCALEDIR', join_paths(get_option('prefix'), get_option('localedir')))
config_h.set_quoted('LOCALEDOMAIN', gettext_domain)
config_h.set_quoted('PACKAGE_DATA_DIR', mod_data_dir)
config_h.set('__UNUSED__', '__attribute__((unused))')

config_dir = include_directories('.')

if get_option('enotify')
   config_h.set('HAVE_ENOTIFY', true)
endif

if get_option('imap2')
   imap2 = true
endif

#### i18n ####
dep_intl = []
if get_option('nls')
   config_h.set('HAVE_GETTEXT', '1')
   dep_intl = cc.find_library('intl', required : false)
   subdir('po')
endif

#### module.desktop ####
install_data('module.desktop',
  install_dir : mod_install_dir
)

##### edje_cc binary compiler tool
edje_cc = get_option('edje-cc')
if edje_cc == ''
edje_cc = find_program('edje_cc')
endif

#### module sources ####
subdir('src')

#### write config file ####
configure_file(output: 'config.h', configuration: config_h)

cmd = [ edje_cc,
        '-id', join_paths(meson.project_source_root(), 'images'),
        '@INPUT@', '@OUTPUT@']
custom_target('e-module-mail.edj',
              input      : 'e-module-mail.edc',
              output     : 'e-module-mail.edj',
              command    : cmd,
              install_dir: mod_install_dir,
              install    : true
             )

custom_target('mail.edj',
              input      : 'mail.edc',
              output     : 'mail.edj',
              command    : cmd,
              install_dir: mod_install_dir,
              install    : true
             )

#### Report ####
if meson.version().version_compare('>=0.53')
   summary({'install': lib_install_dir,
           }, section: 'Directories')
endif
