# Configure Nginx to include a custom HTTP response header
class nginx_custom_http_response_header {
  package { 'nginx':
    ensure => installed,
  }
  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => present,
    content => template('nginx/custom_headers.conf.erb'),
    notify  => Service['nginx'],
  }
  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
  }
}
include nginx_custom_http_response_header
