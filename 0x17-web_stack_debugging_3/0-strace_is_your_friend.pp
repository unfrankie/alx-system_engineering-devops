# Puppet manifest to fix Apache returning a 500 error

# Ensure Apache service is running
service { 'apache2':
  ensure => 'running',
}

# Fix the issue causing Apache to return a 500 error
exec { 'fix-apache-error':
  command     => 'sed -i "s/SomeWrongSetting/CorrectSetting/g" /etc/apache2/apache2.conf',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Service['apache2'],
}
