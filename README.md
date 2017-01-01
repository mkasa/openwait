# Introduction of openwait
openwait enables a couple of remote-to-local operations.
See the examples below.

First we login to a remote host.
```bash
$ rssh remoteuser@remote-host
```
This launches a local process of openwait server, do ssh to the
remote host with port forwarding to the local openwait server.
The port number and a shared secret (session-only one-time password)
are transmitted via an environmental variable.

Open a local browser. This is equivalent to local `open
http://www.yahoo.com/`.

```bash
[remoteuser@remotehost ~]% lopen http://www.yahoo.com/
```

Paste a text from the clipboard on the local host.
```bash
[remoteuser@remotehost ~]% lpaste
```

Copy a text to the clipboard on the local host.

```bash
[remoteuser@remotehost ~]% echo Hello | lcopy
```

Push a file to `~/.openwait/vartmp` of the local host.
```bash
[remoteuser@remotehost ~]% lpush abc.xlsx
```

Push a file to `~/.openwait/vartmp` of the local host, and then `open`
it. We expect MS Excel to open up on the local side in the following example.
```bash
[remoteuser@remotehost ~]% lpush -o abc.xlsx
```

Push a file to the current directory of the local host, and then `open`
it. We expect MS Excel to open up on the local side in the following example.
```bash
[remoteuser@remotehost ~]% lpush -p -o abc.xlsx
```

Push a file to the local host, and then `open` in background.

```bash
[remoteuser@remotehost ~]% lpush -g -o image.png
```

Push a file to the specified directory (`/tmp` in the example below) on the local host.

```bash
[remoteuser@remotehost ~]% lpush -d /tmp image.png
```

Paste an image from the clipboard on the local host.
Copy an image to the clipboard on the local host.
You need [impbpaste/impbcopy](http://www.alecjacobson.com/weblog/?p=3816) for this feature.
```bash
[remoteuser@remotehost ~]% limpaste
[remoteuser@remotehost ~]% limcopy test.png
```

Note that you usually need to edit the server config file
(`~/.openwait/server_config`) to allow poteintally insecure operations
(i.e., most operations).

# Installation
Python 2.x is required. Python 3.x is experimentally supported via 2to3
(not tested).
Before installing openwait, you need a few Python modules.

```bash
$ pip install pyyaml
$ pip isntall python-daemon
$ pip isntall lockfile
```

openwait comes with waf installer, so configure&make&make install.
(actually, make does nothing here).

```bash
$ ./waf configure
$ ./waf build
$ sudo ./waf install
```

If you don't have a root, probably you want to do like this instead of
doing the commands above, in order to install it into `~/local/bin`.

```bash
$ ./waf configure --prefix=$HOME/local/bin
$ ./waf build
$ ./waf install
```

That's it!

# Going through a gateway
rssh can be nested.

```bash
$ rssh gatewayuser@gateway-host
[gatewayuser@gateway-host ~]% rssh iuser@internal-host
[iuser@internal-host ~]% lopen http://www.yahoo.com/
```

Make sure that openwait is installed on all of the remote/local hosts.
openwait server is terminated when the rssh session finishes.
If not, just kill the server process.

# Security
Connections between a remote host and a local host are encrypted by ssh.
Any processes that connect to a local daemon needs a shared secret to do
anything serious. Any user who has a local root can steal the shared
secret. Any user who has a remote root (or your account itself) can
steal the shared secret.

For safety, you can allow only limited operations; you can disable
several features.
Just edit `~/.openwait/server_config` in the local side where you launch (implicitly)
an openwait server. `~/.openwait/server_config` is in YAML format with a lot of
comments. Here is an example configuration.

```
# This is a server config file of openwait
lopen:
  # lopen/enabled: if true, open from a remote host is allowed.
  enabled: true
  # lopen/allow_http_protocol: if true, the URL may start with
'http://'.
  allow_http_protocol: true
  # lopen/allow_https_protocol: if true, the URL may start with
'https://'.
  allow_https_protocol: true
  # lopen/allow_https_protocol: if true, the URL may start with
'file://'.
  allow_file_protocol: false
  # lopen/allow_https_protocol: if true, the URL may start with any
other protocols than the protocols above
  allow_other_protocols: false
  # lopen/filter_non_url_chars: if true, characters not allowed in URLs
are eliminated for security.
  #                             you may want to disable it if you want
to put non-ASCII characters directly in the URL
  filter_non_url_chars: true
lpaste:
  # lpaste/enabled: if false, lpaste is not allowed.
  enabled: false
  # lpaste/max_size: the maximum size of data (in bytes)
  max_size: 16384
limpaste:
  # limpaste/enabled: if false, limpaste is not allowed.
  enabled: false
  # limpaste/max_size: the maximum size of data (in bytes)
  max_size: 10000000
lcopy:
  # lcopy/enabled: if false, lcopy is not allowed.
  enabled: true
  # lcopy/max_size: the maximum size of data (in bytes)
  max_size: 16384
limcopy:
  # limcopy/enabled: if false, limcopy is not allowed.
  enabled: true
  # limcopy/max_size: the maximum size of data (in bytes)
  max_size: 10000000
lpush:
  # lpush/enabled: if false, lpush is not allowed.
  enabled: true
  # lpush/allow_open: if true, the pushed file can be opened if
requested.
  allow_open: true
  # lpush/allow_push_to_tmp: if true, the destination can be an openwait
tmp dir (default: ~/.openwait/vartmp)
  allow_push_to_tmp_dir: true
  # lpush/allow_push_to_current_dir: if true, the destination can be the
current dir.
  allow_push_to_current_dir: true
  # lpush/allow_push_to_any_dir: if true, the destination can be any
directory.
  #     this option is dangerous, so please be careful if you enable it.
  #     for example, it could write to ~/.ssh/authorized_keys.
  allow_push_to_any_dir: true
  # lpush/allow_overwrite: if false, the file cannot be overwritten.
  allow_overwrite: false
  # lpush/max_size: the maximum size of data (in bytes)
  max_size: 10000000
```

# License
MIT License
