#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : websockify
Version  : 0.8.0
Release  : 41
URL      : http://pypi.debian.net/websockify/websockify-0.8.0.tar.gz
Source0  : http://pypi.debian.net/websockify/websockify-0.8.0.tar.gz
Summary  : Websockify.
Group    : Development/Tools
License  : LGPL-3.0
Requires: websockify-bin
Requires: websockify-python3
Requires: websockify-license
Requires: websockify-data
Requires: websockify-python
Requires: numpy
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
websockify was formerly named wsproxy and was part of the

%package bin
Summary: bin components for the websockify package.
Group: Binaries
Requires: websockify-data
Requires: websockify-license

%description bin
bin components for the websockify package.


%package data
Summary: data components for the websockify package.
Group: Data

%description data
data components for the websockify package.


%package license
Summary: license components for the websockify package.
Group: Default

%description license
license components for the websockify package.


%package python
Summary: python components for the websockify package.
Group: Default
Requires: websockify-python3

%description python
python components for the websockify package.


%package python3
Summary: python3 components for the websockify package.
Group: Default
Requires: python3-core

%description python3
python3 components for the websockify package.


%prep
%setup -q -n websockify-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1529094761
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/websockify
cp LICENSE.txt %{buildroot}/usr/share/doc/websockify/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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

%files license
%defattr(-,root,root,-)
/usr/share/doc/websockify/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
