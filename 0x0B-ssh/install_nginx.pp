$package_name = 'nginx'
package {$package_name:
	ensure => installed,
}
service { $package_name:
	ensure => running,
	enable => true,
	require => Package['nginx'],
}
