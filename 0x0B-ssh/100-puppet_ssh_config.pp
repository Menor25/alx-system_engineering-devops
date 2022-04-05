#!/usr/bin/env bash
# Client configuration file (w/ Puppet)
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
