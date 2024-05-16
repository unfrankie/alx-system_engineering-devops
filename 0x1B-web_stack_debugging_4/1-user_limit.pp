# User limit
exec { 'change-os-configuration-for-holberton-user':
  command => 'ulimit -n 65535',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
}
