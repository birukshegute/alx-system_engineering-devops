# Installs flask from pip3 using puppet

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
