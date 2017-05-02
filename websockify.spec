#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websockify
Version  : 0.8.0
Release  : 23
URL      : http://pypi.debian.net/websockify/websockify-0.8.0.tar.gz
Source0  : http://pypi.debian.net/websockify/websockify-0.8.0.tar.gz
Summary  : Websockify.
Group    : Development/Tools
License  : LGPL-3.0
Requires: websockify-bin
Requires: websockify-python
Requires: websockify-data
Requires: numpy
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
## websockify: WebSockets support for any application/server
websockify was formerly named wsproxy and was part of the
[noVNC](https://github.com/kanaka/noVNC) project.

%package bin
Summary: bin components for the websockify package.
Group: Binaries
Requires: websockify-data

%description bin
bin components for the websockify package.


%package data
Summary: data components for the websockify package.
Group: Data

%description data
data components for the websockify package.


%package python
Summary: python components for the websockify package.
Group: Default

%description python
python components for the websockify package.


%prep
%setup -q -n websockify-0.8.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490215582
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1490215582
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/websockify

%files data
%defattr(-,root,root,-)
/usr/share/websockify/include/base64.js
/usr/share/websockify/include/util.js
/usr/share/websockify/include/web-socket-js/WebSocketMain.swf
/usr/share/websockify/include/web-socket-js/swfobject.js
/usr/share/websockify/include/web-socket-js/web_socket.js
/usr/share/websockify/include/websock.js

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
