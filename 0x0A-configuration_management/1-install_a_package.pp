# Install Flask package 2.1.0

class { 'python':
  version => '3.8.10'
}

package { 'python3-pip':
  ensure   => 'present',
  provider => 'pip3',
  require  => Class['python']
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip']
}
