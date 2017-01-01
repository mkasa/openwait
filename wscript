APPNAME = 'openwait'
VERSION = '1.0.0'

srcdir = '.'
blddir = 'build'

def configure(conf):
    conf.load('python')

def build(bld):
    bld.install_files(
        '${PREFIX}/bin', [
        'openwait',
        'rssh',
        ], chmod=0755)
    bld.symlink_as('${PREFIX}/bin/lopen'   , 'openwait')
    bld.symlink_as('${PREFIX}/bin/lcopy'   , 'openwait')
    bld.symlink_as('${PREFIX}/bin/lpaste'  , 'openwait')
    bld.symlink_as('${PREFIX}/bin/limcopy' , 'openwait')
    bld.symlink_as('${PREFIX}/bin/limpaste', 'openwait')
    bld.symlink_as('${PREFIX}/bin/lpush'   , 'openwait')

def dist(ctx):
   ctx.algo = 'tar.gz'
   # ctx.files = ctx.path.ant_glob([])
