APPNAME = 'openwait'
VERSION = '1.0.1'

srcdir = '.'
blddir = 'build'

def configure(conf):
    conf.load('python')
    conf.check_python_version(minver=(2, 7))
    conf.check_python_module('lockfile')
    conf.check_python_module('yaml')
    conf.check_python_module('daemon')
    import os, sys
    if conf.env['PYTHON_VERSION'].startswith("3."):
        sys.stderr.write("Python version is " + conf.env['PYTHON_VERSION'] + ".x, so use 2to3.\n")
        import subprocess
        subprocess.check_call(['2to3', '-w', 'openwait'])
        subprocess.check_call(['2to3', '-w', 'lopen'])

def build(bld):
    bld.install_files(
        '${PREFIX}/bin', [
        'openwait',
        'lopen',
        'rssh',
        ], chmod=0755)
    bld.symlink_as('${PREFIX}/bin/lcopy'   , 'lopen')
    bld.symlink_as('${PREFIX}/bin/lpaste'  , 'lopen')
    bld.symlink_as('${PREFIX}/bin/limcopy' , 'lopen')
    bld.symlink_as('${PREFIX}/bin/limpaste', 'lopen')
    bld.symlink_as('${PREFIX}/bin/lpush'   , 'lopen')

def dist(ctx):
   ctx.algo = 'tar.gz'
   # ctx.files = ctx.path.ant_glob([])
