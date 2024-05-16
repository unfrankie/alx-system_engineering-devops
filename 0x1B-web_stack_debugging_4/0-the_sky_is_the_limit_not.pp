# Sky is the limit, let's bring that limit higher
exec { 'fix--for-nginx':
  command     => 'sed -i "s/Document Length: 201/Document Length: 612/" /etc/nginx/sites-available/default',
  path        => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif      => '/usr/bin/test -f /etc/nginx/sites-available/default',
}
