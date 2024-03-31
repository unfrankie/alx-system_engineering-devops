# Configure Nginx to include a custom HTTP response header
exec { 'update_package_lists':
  command     => '/usr/bin/apt-get update',
  refreshonly => true,
}
package { 'nginx':
  ensure => installed,
  require => Exec['update_package_lists'],
}
file_line { 'header_served_by':
  path     => '/etc/nginx/sites-available/default',
  match    => '^server {',
  line     => "server {\n\tadd_header X-Served-By \"${hostname}\";",
  multiple => false,
  require  => Package['nginx'],
  notify   => Exec['restart_nginx'],
}
exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
