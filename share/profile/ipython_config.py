# IPerl VERSION
c = get_config()
#c.KernelManager.kernel_cmd = ['perl', '-MDevel::IPerl', '-e1', 'kernel', '{connection_file}']
c.KernelManager.kernel_spec = 'iperl'
c.Session.key = b''
c.Session.keyfile = b''

# Syntax highlight for Perl notebooks.
c.NbConvertBase.default_language = "perl"
