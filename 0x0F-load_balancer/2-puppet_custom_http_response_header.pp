# Configure Nginx to include a custom HTTP response header
exec {'update packages':
  provider => shell,
  command  => 'sudo apt-get update -y',
  before   => Exec['install Nginx'],
}
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get install nginx -y',
  before   => Exec['Custom HTTP Header'],
}
exec { 'Custom HTTP Header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['Restart Nginx services'],
}
exec { 'Restart Nginx services':
  provider => shell,
  command  => 'sudo service nginx restart',
}
