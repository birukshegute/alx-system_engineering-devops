# Installs flask from pip3 using puppet

package { 'flask':
  ensure          => installed,
  provider        => 'pip3',
}
