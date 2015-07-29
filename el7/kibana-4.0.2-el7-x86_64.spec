%define debug_package %{nil}
Name:		kibana
Version:	4.0.2
Release:	1%{?dist}
Summary:	Graphical interface to Elasticsearch to enable the exploration and visualization of any kind of data.

Group:		Applications/Internet
License:	Apache 2.0
URL:		https://www.elastic.co/products/kibana
Source0:	https://download.elastic.co/kibana/kibana/kibana-4.0.2-linux-x64.tar.gz
Source1:	kibana.service
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:	elasticsearch
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
Kibana is a browser based analytics and search interface for Elasticsearch that was developed primarily to view Logstash event data.

%prep
%setup -q -n kibana-4.0.2-linux-x64

%pre
/usr/bin/getent group kibana || /usr/sbin/groupadd -r kibana
/usr/bin/getent passwd kibana || /usr/sbin/useradd -g kibana -r -d /opt/kibana -s /sbin/nologin kibana

%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/opt/kibana
cp -aR bin/ %{buildroot}/opt/kibana
cp -aR config/ %{buildroot}/opt/kibana
cp -aR node/ %{buildroot}/opt/kibana
cp -aR plugins/ %{buildroot}/opt/kibana
cp -aR src/ %{buildroot}/opt/kibana
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 755 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/kibana.service


%clean
rm -rf %{buildroot}

%post
systemctl daemon-reload

%preun
systemctl stop %{name} >/dev/null 2>&1

%files
%defattr(-,root,root,-)
%dir /opt/kibana/bin
%attr(755,root,root) /opt/kibana/bin/kibana
/opt/kibana/bin/kibana.bat
/opt/kibana/node
/opt/kibana/plugins
/opt/kibana/src
/usr/lib/systemd/system/kibana.service
%dir /opt/kibana/config
%config /opt/kibana/config/kibana.yml
