# Installs flask from pip3 using puppet

exec { 'Flask':
  command => '/usr/bin/apt-get -y install Flask -v 2.1.0',
}
