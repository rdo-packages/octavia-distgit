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
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  systemd
BuildRequires:  openstack-macros

# BuildRequires for running functional tests
BuildRequires:  python2-stestr
BuildRequires:  python-requests-mock
BuildRequires:  python2-mock
BuildRequires:  python2-subunit
BuildRequires:  python2-oslotest
BuildRequires:  python2-testrepository
BuildRequires:  python2-testtools
BuildRequires:  python2-testresources
BuildRequires:  python2-testscenarios
BuildRequires:  python2-oslo-utils
BuildRequires:  python-flask
BuildRequires:  python2-oslo-config
BuildRequires:  python-netifaces
BuildRequires:  python2-oslo-log
BuildRequires:  python2-glanceclient
BuildRequires:  python2-wsme
BuildRequires:  python2-barbicanclient
BuildRequires:  python2-cryptography
BuildRequires:  python2-gunicorn
BuildRequires:  python2-keystoneauth1
BuildRequires:  python-futures
BuildRequires:  python2-netaddr
BuildRequires:  python2-novaclient
BuildRequires:  python2-taskflow
BuildRequires:  python2-neutronclient
BuildRequires:  python2-oslo-db
BuildRequires:  python2-oslo-reports
BuildRequires:  python2-oslo-policy
BuildRequires:  python2-pecan
BuildRequires:  python2-pyroute2
BuildRequires:  python2-pyasn1
BuildRequires:  python2-oslo-messaging
BuildRequires:  python2-pyasn1-modules
BuildRequires:  python2-cotyledon
BuildRequires:  python2-keystonemiddleware
BuildRequires:  python-werkzeug
BuildRequires:  python2-distro

Requires:   python-%{service} = %{version}-%{release}

Requires(pre): shadow-utils
%{?systemd_requires}

%description
%{common_desc}


%package -n python-%{service}
Summary:    Octavia Python libraries
Group:      Applications/System

BuildArch:  noarch

Requires:   python2-alembic >= 0.8.10
Requires:   python2-pecan >= 1.0.0
Requires:   python2-pbr >= 2.0.0
Requires:   python2-sqlalchemy >= 1.0.10
Requires:   python2-babel >= 2.3.4
Requires:   python2-requests >= 2.14.2
Requires:   python2-keystonemiddleware >= 4.17.0
Requires:   python2-netaddr >= 0.7.18
Requires:   python2-neutronclient >= 6.3.0
Requires:   python-webob >= 1.7.1
Requires:   python2-six >= 1.10.0
Requires:   python2-stevedore >= 1.20.0
Requires:   python2-oslo-config >= 2:5.1.0
Requires:   python2-oslo-context >= 2.19.2
Requires:   python2-oslo-db >= 4.27.0
Requires:   python2-oslo-i18n >= 3.15.3
Requires:   python2-oslo-serialization >= 2.18.0
Requires:   python2-oslo-log >= 3.36.0
Requires:   python2-oslo-messaging >= 5.29.0
Requires:   python2-oslo-middleware >= 3.31.0
Requires:   python2-oslo-policy >= 1.30.0
Requires:   python2-oslo-utils >= 3.33.0
Requires:   python2-barbicanclient >= 4.5.2
Requires:   python2-novaclient >= 9.1.0
Requires:   pyOpenSSL >= 17.1.0
Requires:   python2-wsme
Requires:   python2-pyasn1
Requires:   python2-pyasn1-modules
Requires:   python2-jinja2 >= 2.10
Requires:   python2-taskflow >= 2.16.0
Requires:   python-flask >= 0.10
Requires:   python-netifaces >= 0.10.4
Requires:   python2-cryptography >= 2.1
Requires:   python2-keystoneauth1 >= 3.3.0
Requires:   python2-oslo-reports >= 1.18.0
Requires:   python2-glanceclient >= 1:2.8.0
Requires:   python2-rfc3986
Requires:   python2-pyroute2 >= 0.4.21
Requires:   python-ipaddress >= 1.0.16
Requires:   python2-gunicorn >= 19.0
Requires:   python2-cotyledon >= 1.3.0
Requires:   python-werkzeug >= 0.9
Requires:   python2-distro >= 1.2.0

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
Requires:   python2-mock
Requires:   python2-subunit
Requires:   python2-oslotest
Requires:   python2-testrepository
Requires:   python2-testtools
Requires:   python2-testresources
Requires:   python2-testscenarios
Requires:   python2-tempest
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

# Move policy.json to proper location
mv etc/policy/admin_or_owner-policy.json %{buildroot}%{_sysconfdir}/%{service}/policy.json

# Install logrotate
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/openstack-%{service}
install -p -D -m 644 elements/amphora-agent/install.d/amphora-agent-source-install/amphora-agent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/openstack-%{service}-amphora-agent

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
stestr run

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
%config(noreplace) %attr(0640, root, %{service}) %{_sysconfdir}/%{service}/policy.json
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
