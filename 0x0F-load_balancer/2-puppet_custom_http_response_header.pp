# configures a brand new Ubuntu machine to the requirements
exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => 'add_header X-Served-By $hostname;'
}
-> exec {'run2':
  command => '/usr/sbin/service nginx start',
}
