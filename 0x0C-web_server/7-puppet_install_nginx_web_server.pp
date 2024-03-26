# Install and configures Nginx web server
package { 'nginx':
  ensure => installed,
}
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}
file { '/etc/nginx/sites-available/redirect_me':
  ensure  => present,
  content => "server {
    listen 80;
    server_name _;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}",
}
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect_me',
}
file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
}
file { '/etc/nginx/sites-available/custom_404':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    server_name _;
    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }
}",
}
file { '/etc/nginx/sites-enabled/custom_404':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_404',
}
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/redirect_me', '/etc/nginx/sites-enabled/custom_404'],
}
