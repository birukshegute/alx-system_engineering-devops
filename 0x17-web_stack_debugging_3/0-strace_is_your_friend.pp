# updates wrong `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'update-phpp-to-php':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
