# To the LD_LIBRARY_PATH, we add libfoo.so path
file { ‘/etc/profile.d/custom_ld_library_path.sh’:
ensure => present,
content => ‘export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path/to/libfoo’,
mode => ‘0644’,
}
# Restart Apache
service { ‘apache2’:
ensure => running,
subscribe => File[‘/etc/profile.d/custom_ld_library_path.sh’],
}
