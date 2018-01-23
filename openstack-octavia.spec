%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service octavia
%global common_desc Octavia is an Operator-grade open source scalable load balancer.

Name:       openstack-%{service}
Version:    XXX
Release:    XXX
Summary:    Octavia, a load balancer implementation for OpenStack

License:    ASL 2.0
URL:        http://launchpad.net/%{service}/

Source0:    https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
Source1:    %{service}.logrotate
Source10:   %{service}-amphora-agent.service
Source11:   %{service}-api.service
Source12:   %{service}-worker.service
Source13:   %{service}-health-manager.service
Source14:   %{service}-housekeeping.service

Source30:   %{service}-dist.conf

BuildRequires:  python2-devel
BuildRequires:  python-d2to1
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  systemd-units
BuildRequires:  openstack-macros

# BuildRequires for running functional tests
BuildRequires:  python-requests-mock
BuildRequires:  python-mock
BuildRequires:  python-subunit
BuildRequires:  python-oslotest
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
BuildRequires:  python-testresources
BuildRequires:  python-testscenarios
BuildRequires:  python-oslo-utils
BuildRequires:  python-flask
BuildRequires:  python-oslo-config
BuildRequires:  python-netifaces
BuildRequires:  python-oslo-log
BuildRequires:  python-glanceclient
BuildRequires:  python-wsme
BuildRequires:  python-barbicanclient
BuildRequires:  python-cryptography
BuildRequires:  python-gunicorn
BuildRequires:  python-keystoneauth1
BuildRequires:  python-futures
BuildRequires:  python-netaddr
BuildRequires:  python-novaclient
BuildRequires:  python-taskflow
BuildRequires:  python-neutronclient
BuildRequires:  python-oslo-db
BuildRequires:  python-oslo-reports
BuildRequires:  python-oslo-policy
BuildRequires:  python-pecan
BuildRequires:  python-pyroute2
BuildRequires:  python-pyasn1
BuildRequires:  python-oslo-messaging
BuildRequires:  python-pyasn1-modules
BuildRequires:  python-cotyledon
BuildRequires:  python-keystonemiddleware

Requires:   python-%{service} = %{version}-%{release}

Requires(pre): shadow-utils
%{?systemd_requires}

%description
%{common_desc}


%package -n python-%{service}
Summary:    Octavia Python libraries
Group:      Applications/System

BuildArch:  noarch

Requires:   python-alembic >= 0.8.7
Requires:   python-pecan >= 1.0.0
Requires:   python-pbr >= 2.0.0
Requires:   python-sqlalchemy >= 1.0.10
Requires:   python-babel >= 2.3.4
Requires:   python-requests >= 2.10.0
Requires:   python-keystonemiddleware >= 4.12.0
Requires:   python-netaddr >= 0.7.12
Requires:   python-neutronclient >= 6.3.0
Requires:   python-webob >= 1.7.1
Requires:   python-six >= 1.9.0
Requires:   python-stevedore >= 1.20.0
Requires:   python-oslo-config >= 2:4.0.0
Requires:   python-oslo-context >= 2.14.0
Requires:   python-oslo-db >= 4.24.0
Requires:   python-oslo-i18n >= 2.1.0
Requires:   python-oslo-serialization >= 1.10.0
Requires:   python-oslo-log >= 3.22.0
Requires:   python-oslo-messaging >= 5.24.2
Requires:   python-oslo-middleware >= 3.27.0
Requires:   python-oslo-policy >= 1.23.0
Requires:   python-oslo-utils >= 3.20.0
Requires:   python-barbicanclient >= 4.0.0
Requires:   python-novaclient >= 1:9.0.0
Requires:   pyOpenSSL >= 0.14
Requires:   python-wsme
Requires:   python-pyasn1
Requires:   python-pyasn1-modules
Requires:   python-jinja2 >= 2.7.2
Requires:   python-taskflow >= 2.7.0
Requires:   python-flask >= 0.10
Requires:   python-netifaces >= 0.10.4
Requires:   python-cryptography >= 1.6
Requires:   python-keystoneauth1 >= 3.1.0
Requires:   python-oslo-reports >= 0.6.0
Requires:   python-glanceclient >= 1:2.8.0
Requires:   python-rfc3986
Requires:   python-pyroute2 >= 0.4.3
Requires:   python-ipaddress >= 1.0.7
Requires:   python-gunicorn >= 19.0
Requires:   python-cotyledon >= 1.3.0

%description -n python-%{service}
%{common_desc}

This package contains the Octavia Python library.

%package -n python-%{service}-tests
Summary:    Octavia tests
Group:      Applications/System

BuildArch: noarch

Requires:   python-%{service} = %{version}-%{release}
Requires:   python-%{service}-tests-golang = %{version}-%{release}

Requires:   python-requests-mock
Requires:   python-mock
Requires:   python-subunit
Requires:   python-oslotest
Requires:   python-testrepository
Requires:   python-testtools
Requires:   python-testresources
Requires:   python-testscenarios
Requires:   python-tempest
Requires:   python-futures

%description -n python-%{service}-tests
%{common_desc}

This package contains Octavia test files.

%package -n python-%{service}-tests-golang
Summary:    Octavia tests golang

BuildRequires:   golang
BuildRequires:   glibc-static

%description -n python-%{service}-tests-golang
%{common_desc}

This package contains Octavia tempest golang httpd code.

%package common
Summary:    Octavia common files
Group:      Applications/System

BuildArch: noarch

Requires:   python-%{service} = %{version}-%{release}


%description common
%{common_desc}

This package contains Octavia files common to all services.



%package amphora-agent
Summary:    OpenStack Octavia Amphora Agent service
Group:      Applications/System

BuildArch: noarch
Requires:   openstack-%{service}-common = %{version}-%{release}


%description amphora-agent
%{common_desc}

This package contains OpenStack Octavia Amphora Agent service.



%package api
Summary:    OpenStack Octavia API service
Group:      Applications/System
BuildArch: noarch

Requires:   openstack-%{service}-common = %{version}-%{release}


%description api
%{common_desc}

This package contains OpenStack Octavia API service.


%package worker
Summary:    OpenStack Octavia Consumer service
Group:      Applications/System

BuildArch: noarch

Requires:   openstack-%{service}-common = %{version}-%{release}


%description worker
%{common_desc}

This package contains OpenStack Octavia Consumer service.


%package health-manager
Summary:    OpenStack Octavia Health-Manager service
Group:      Applications/System

BuildArch: noarch

Requires:   openstack-%{service}-common = %{version}-%{release}


%description health-manager
%{common_desc}

This package contains OpenStack Octavia Health-Manager service.


%package housekeeping
Summary:    OpenStack Octavia Housekeeping service
Group:      Applications/System

BuildArch: noarch
Requires:   openstack-%{service}-common = %{version}-%{release}


%description housekeeping
%{common_desc}

This package contains OpenStack Octavia Housekeeping service.


%package diskimage-create
Summary:    OpenStack Octavia Amphora diskimage-builder script
Group:      Applications/System

BuildArch: noarch

Requires:   openstack-%{service}-common = %{version}-%{release}
Requires:   dib-utils
Requires:   diskimage-builder >= 1.18.0


%description diskimage-create
%{common_desc}

This package contains a diskimage-builder script for creating Octavia Amphora images



%prep
%setup -q -n %{service}-%{upstream_version}

find %{service} -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Let's handle dependencies ourseleves
rm -f requirements.txt


%build
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{__python2} setup.py build

# Generate octavia-tests-httpd binary from httpd.go
pushd %{service}/tests/contrib
 go build -ldflags '-linkmode external -extldflags -static' -o %{service}-tests-httpd httpd.go
popd

# Loop through values in octavia-dist.conf and make sure that the values
# are substituted into the octavia.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/%{service}.conf
done < %{SOURCE30}

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Move httpd binary to proper place
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 %{service}/tests/contrib/%{service}-tests-httpd %{buildroot}%{_bindir}

# Replace the path with its binary
PATH1=%{buildroot}%{python2_sitelib}/%{service}/tests/tempest/v1/scenario/base.py
PATH2=%{buildroot}%{python2_sitelib}/%{service}/tests/tempest/v2/scenario/base.py
sed -i "s#self._build_static_httpd()#'/usr/bin/%{service}-tests-httpd'#g" $PATH1
sed -i "s#self._build_static_httpd()#'/usr/bin/%{service}-tests-httpd'#g" $PATH2

# Remove httpd.go code
rm  %{buildroot}%{python2_sitelib}/%{service}/tests/contrib/httpd.go

# Create fake egg-info for the tempest plugin
%py2_entrypoint %{service} %{service}

# Remove unused files
rm -rf %{buildroot}%{python2_sitelib}/bin
rm -rf %{buildroot}%{python2_sitelib}/doc
rm -rf %{buildroot}%{python2_sitelib}/tools

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/%{service}
mv %{buildroot}/usr/etc/%{service}/%{service}.conf %{buildroot}%{_sysconfdir}/%{service}

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-%{service}
install -p -D -m 644 elements/amphora-agent/static/etc/logrotate.d/amphora-agent %{buildroot}%{_sysconfdir}/logrotate.d/openstack-%{service}-amphora-agent

# Install systemd units
install -p -D -m 644 %{SOURCE10} %{buildroot}%{_unitdir}/%{service}-amphora-agent.service
install -p -D -m 644 %{SOURCE11} %{buildroot}%{_unitdir}/%{service}-api.service
install -p -D -m 644 %{SOURCE12} %{buildroot}%{_unitdir}/%{service}-worker.service
install -p -D -m 644 %{SOURCE13} %{buildroot}%{_unitdir}/%{service}-health-manager.service
install -p -D -m 644 %{SOURCE14} %{buildroot}%{_unitdir}/%{service}-housekeeping.service

# Setup directories
install -d -m 755 %{buildroot}%{_datadir}/%{service}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{service}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{service}
install -d -m 755 %{buildroot}%{_localstatedir}/run/%{service}

# Install dist conf
install -p -D -m 640 %{SOURCE30} %{buildroot}%{_datadir}/%{service}/%{service}-dist.conf


# Create configuration directories for all services that can be populated by users with custom *.conf files
mkdir -p %{buildroot}/%{_sysconfdir}/%{service}/conf.d/common
for service in amphora-agent api health-manager housekeeping worker; do
    mkdir -p %{buildroot}/%{_sysconfdir}/%{service}/conf.d/%{service}-$service
done

# Install diskimage-create files
cp -vr elements/ %{buildroot}%{_datadir}/%{service}-image-elements
install -m 755 diskimage-create/diskimage-create.sh %{buildroot}%{_bindir}/%{service}-diskimage-create.sh
# Remove setuptools installed diskimage-create files
rm -rf %{buildroot}%{_datadir}/%{service}/diskimage-create
rm -rf %{buildroot}%{_datadir}/%{service}/LICENSE
rm -rf %{buildroot}%{_datadir}/%{service}/README.rst

%pre common
getent group %{service} >/dev/null || groupadd -r %{service}
getent passwd %{service} >/dev/null || \
    useradd -r -g %{service} -d %{_sharedstatedir}/%{service} -s /sbin/nologin \
    -c "OpenStack Octavia Daemons" %{service}
exit 0

%check
export OS_TEST_PATH='./%{service}/tests/functional'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
%{__python2} setup.py testr

%post amphora-agent
%systemd_post %{service}-amphora-agent.service


%preun amphora-agent
%systemd_preun %{service}-amphora-agent.service


%postun amphora-agent
%systemd_postun_with_restart %{service}-amphora-agent.service


%post api
%systemd_post %{service}-api.service


%preun api
%systemd_preun %{service}-api.service


%postun api
%systemd_postun_with_restart %{service}-api.service


%post worker
%systemd_post %{service}-worker.service


%preun worker
%systemd_preun %{service}-worker.service


%postun worker
%systemd_postun_with_restart %{service}-worker.service


%post health-manager
%systemd_post %{service}-health-manager.service


%preun health-manager
%systemd_preun %{service}-health-manager.service


%postun health-manager
%systemd_postun_with_restart %{service}-health-manager.service


%post housekeeping
%systemd_post %{service}-housekeeping.service


%preun housekeeping
%systemd_preun %{service}-housekeeping.service


%postun housekeeping
%systemd_postun_with_restart %{service}-housekeeping.service

# Create a tempest plugin fake egg-info file
%files -n python-%{service}-tests
%license LICENSE
%{python2_sitelib}/%{service}/tests
%{python2_sitelib}/%{service}_tests.egg-info

%files -n python-%{service}-tests-golang
%{_bindir}/%{service}-tests-httpd

%files -n python-%{service}
%license LICENSE
%{python2_sitelib}/%{service}
%{python2_sitelib}/%{service}-*.egg-info
%exclude %{python2_sitelib}/%{service}/tests


%files common
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/%{service}/conf.d
%dir %{_sysconfdir}/%{service}/conf.d/common
%attr(-, root, %{service}) %{_datadir}/%{service}/%{service}-dist.conf
%config(noreplace) %attr(0640, root, %{service}) %{_sysconfdir}/%{service}/%{service}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-%{service}
%dir %attr(0755, %{service}, %{service}) %{_sharedstatedir}/%{service}
%dir %attr(0750, %{service}, %{service}) %{_localstatedir}/log/%{service}
%dir %{_datarootdir}/%{service}
%{_bindir}/haproxy-vrrp-check
%{_bindir}/%{service}-db-manage

%files amphora-agent
%license LICENSE
%{_bindir}/amphora-agent
%{_unitdir}/%{service}-amphora-agent.service
%dir %{_sysconfdir}/%{service}/conf.d/%{service}-amphora-agent
%config(noreplace) %{_sysconfdir}/logrotate.d/openstack-%{service}-amphora-agent


%files api
%license LICENSE
%{_bindir}/%{service}-api
%{_bindir}/%{service}-wsgi
%{_unitdir}/%{service}-api.service
%dir %{_sysconfdir}/%{service}/conf.d/%{service}-api


%files worker
%license LICENSE
%{_bindir}/%{service}-worker
%{_unitdir}/%{service}-worker.service
%dir %{_sysconfdir}/%{service}/conf.d/%{service}-worker


%files health-manager
%license LICENSE
%{_bindir}/%{service}-health-manager
%{_unitdir}/%{service}-health-manager.service
%dir %{_sysconfdir}/%{service}/conf.d/%{service}-health-manager


%files housekeeping
%license LICENSE
%{_bindir}/%{service}-housekeeping
%{_unitdir}/%{service}-housekeeping.service
%dir %{_sysconfdir}/%{service}/conf.d/%{service}-housekeeping

%files diskimage-create
%doc diskimage-create/README.rst
%{_bindir}/%{service}-diskimage-create.sh
%{_datadir}/%{service}-image-elements


%changelog

# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/octavia/commit/?id=0949ee1b3c3616dd342732b937370c5d72fe9b51
