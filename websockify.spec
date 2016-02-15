#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websockify
Version  : 0.7.0
Release  : 13
URL      : https://pypi.python.org/packages/source/w/websockify/websockify-0.7.0.tar.gz
Source0  : https://pypi.python.org/packages/source/w/websockify/websockify-0.7.0.tar.gz
Summary  : Websockify.
Group    : Development/Tools
License  : LGPL-3.0
Requires: websockify-bin
Requires: websockify-python
Requires: websockify-data
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
%setup -q -n websockify-0.7.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

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
/usr/lib/python*/*
