# fix our stack so that we get to 0 failed requests.
exec { 'fix-`our-stack':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
