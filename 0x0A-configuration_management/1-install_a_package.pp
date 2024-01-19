# Installs flask from pip3 using puppet

include python::flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
