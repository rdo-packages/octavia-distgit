# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service octavia
%global common_desc Octavia is an Operator-grade open source scalable load balancer.

Name:       openstack-%{service}
Version:    5.0.2
Release:    1%{?dist}
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

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  systemd
BuildRequires:  openstack-macros
BuildRequires:  git

# BuildRequires for running functional tests
BuildRequires:  python%{pyver}-stestr
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-subunit
BuildRequires:  python%{pyver}-oslotest
BuildRequires:  python%{pyver}-testrepository
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-testresources
BuildRequires:  python%{pyver}-testscenarios
BuildRequires:  python%{pyver}-oslo-utils
BuildRequires:  python%{pyver}-oslo-upgradecheck
BuildRequires:  python%{pyver}-flask
BuildRequires:  python%{pyver}-oslo-config
BuildRequires:  python%{pyver}-oslo-log
BuildRequires:  python%{pyver}-glanceclient
BuildRequires:  python%{pyver}-wsme
BuildRequires:  python%{pyver}-barbicanclient
BuildRequires:  python%{pyver}-cryptography
BuildRequires:  python%{pyver}-gunicorn
BuildRequires:  python%{pyver}-keystoneauth1
BuildRequires:  python%{pyver}-netaddr
BuildRequires:  python%{pyver}-novaclient
BuildRequires:  python%{pyver}-taskflow
BuildRequires:  python%{pyver}-neutronclient
BuildRequires:  python%{pyver}-oslo-db
BuildRequires:  python%{pyver}-oslo-reports
BuildRequires:  python%{pyver}-oslo-policy
BuildRequires:  python%{pyver}-pecan
BuildRequires:  python%{pyver}-pyroute2
BuildRequires:  python%{pyver}-pyasn1
BuildRequires:  python%{pyver}-oslo-messaging
BuildRequires:  python%{pyver}-pyasn1-modules
BuildRequires:  python%{pyver}-cotyledon
BuildRequires:  python%{pyver}-keystonemiddleware
BuildRequires:  python%{pyver}-werkzeug
BuildRequires:  python%{pyver}-distro
BuildRequires:  python%{pyver}-castellan
BuildRequires:  python%{pyver}-octavia-lib >= 1.3.1
BuildRequires:  python%{pyver}-debtcollector
BuildRequires:  python%{pyver}-cinderclient

# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python-requests-mock
BuildRequires:  python-netifaces
BuildRequires:  python-futures
%else
BuildRequires:  python%{pyver}-requests-mock
BuildRequires:  python%{pyver}-netifaces
%endif

Requires:   python%{pyver}-%{service} = %{version}-%{release}

Requires(pre): shadow-utils
%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description
%{common_desc}


%package -n python%{pyver}-%{service}
Summary:    Octavia Python libraries
%{?python_provide:%python_provide python%{pyver}-%{service}}
Group:      Applications/System


Requires:   python%{pyver}-alembic >= 0.8.10
Requires:   python%{pyver}-pecan >= 1.1.0
Requires:   python%{pyver}-pbr >= 2.0.0
Requires:   python%{pyver}-sqlalchemy >= 1.0.10
Requires:   python%{pyver}-babel >= 2.3.4
Requires:   python%{pyver}-requests >= 2.14.2
Requires:   python%{pyver}-keystonemiddleware >= 4.17.0
Requires:   python%{pyver}-netaddr >= 0.7.19
Requires:   python%{pyver}-neutronclient >= 6.7.0
Requires:   python%{pyver}-webob >= 1.7.1
Requires:   python%{pyver}-six >= 1.10.0
Requires:   python%{pyver}-stevedore >= 1.20.0
Requires:   python%{pyver}-oslo-config >= 2:5.2.0
Requires:   python%{pyver}-oslo-context >= 2.19.2
Requires:   python%{pyver}-oslo-db >= 4.27.0
Requires:   python%{pyver}-oslo-i18n >= 3.15.3
Requires:   python%{pyver}-oslo-serialization >= 2.18.0
Requires:   python%{pyver}-oslo-log >= 3.36.0
Requires:   python%{pyver}-oslo-messaging >= 6.3.0
Requires:   python%{pyver}-oslo-middleware >= 3.31.0
Requires:   python%{pyver}-oslo-policy >= 1.30.0
Requires:   python%{pyver}-oslo-utils >= 3.33.0
Requires:   python%{pyver}-oslo-upgradecheck >= 0.1.0
Requires:   python%{pyver}-barbicanclient >= 4.5.2
Requires:   python%{pyver}-novaclient >= 1:9.1.0
Requires:   python%{pyver}-pyOpenSSL >= 17.1.0
Requires:   python%{pyver}-wsme >= 0.8.0
Requires:   python%{pyver}-pyasn1 >= 0.1.8
Requires:   python%{pyver}-pyasn1-modules >= 0.0.6
Requires:   python%{pyver}-jinja2 >= 2.10
Requires:   python%{pyver}-taskflow >= 2.16.0
Requires:   python%{pyver}-flask >= 0.10
Requires:   python%{pyver}-cryptography >= 2.1
Requires:   python%{pyver}-keystoneauth1 >= 3.4.0
Requires:   python%{pyver}-oslo-reports >= 1.18.0
Requires:   python%{pyver}-glanceclient >= 1:2.8.0
Requires:   python%{pyver}-rfc3986 >= 0.3.1
Requires:   python%{pyver}-pyroute2 >= 0.4.21
Requires:   python%{pyver}-gunicorn >= 19.9.0
Requires:   python%{pyver}-cotyledon >= 1.3.0
Requires:   python%{pyver}-werkzeug >= 0.14.1
Requires:   python%{pyver}-distro >= 1.2.0
Requires:   python%{pyver}-castellan >= 0.16.0
Requires:   python%{pyver}-PyMySQL >= 0.7.6
Requires:   python%{pyver}-futurist >= 1.2.0
Requires:   python%{pyver}-tenacity >= 5.0.4
Requires:   python%{pyver}-octavia-lib >= 1.3.1
Requires:   python%{pyver}-debtcollector >= 1.19.0
Requires:   python%{pyver}-jsonschema >= 2.6.0
Requires:   python%{pyver}-cinderclient >= 3.3.0
Requires:   python%{pyver}-setproctitle >= 1.1.10
Requires:   python%{pyver}-simplejson >= 3.13.2

# Handle python2 exception
%if %{pyver} == 2
Requires:   python-netifaces >= 0.10.4
Requires:   python-ipaddress >= 1.0.17
Requires:   python-futures >= 3.0.0
%else
Requires:   python%{pyver}-netifaces >= 0.10.4
%endif


%description -n python%{pyver}-%{service}
%{common_desc}

This package contains the Octavia Python library.

%package -n python%{pyver}-%{service}-tests
Summary:    Octavia tests
%{?python_provide:%python_provide python%{pyver}-%{service}-tests}
Group:      Applications/System

Requires:   python%{pyver}-%{service} = %{version}-%{release}

Requires:   python%{pyver}-mock
Requires:   python%{pyver}-subunit
Requires:   python%{pyver}-oslotest
Requires:   python%{pyver}-testrepository
Requires:   python%{pyver}-testtools
Requires:   python%{pyver}-testresources
Requires:   python%{pyver}-testscenarios
Requires:   python%{pyver}-tempest

# Handle python2 exception
%if %{pyver} == 2
Requires:   python-requests-mock
Requires:   python-futures
%else
Requires:   python%{pyver}-requests-mock
%endif

%description -n python%{pyver}-%{service}-tests
%{common_desc}

This package contains Octavia test files.

%package common
Summary:    Octavia common files
Group:      Applications/System

Requires:   python%{pyver}-%{service} = %{version}-%{release}


%description common
%{common_desc}

This package contains Octavia files common to all services.



%package amphora-agent
Summary:    OpenStack Octavia Amphora Agent service
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}


%description amphora-agent
%{common_desc}

This package contains OpenStack Octavia Amphora Agent service.



%package api
Summary:    OpenStack Octavia API service
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}


%description api
%{common_desc}

This package contains OpenStack Octavia API service.


%package worker
Summary:    OpenStack Octavia Consumer service
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}


%description worker
%{common_desc}

This package contains OpenStack Octavia Consumer service.


%package health-manager
Summary:    OpenStack Octavia Health-Manager service
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}


%description health-manager
%{common_desc}

This package contains OpenStack Octavia Health-Manager service.


%package housekeeping
Summary:    OpenStack Octavia Housekeeping service
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}


%description housekeeping
%{common_desc}

This package contains OpenStack Octavia Housekeeping service.


%package diskimage-create
Summary:    OpenStack Octavia Amphora diskimage-builder script
Group:      Applications/System

Requires:   openstack-%{service}-common = %{version}-%{release}
Requires:   dib-utils
Requires:   diskimage-builder >= 1.1.2


%description diskimage-create
%{common_desc}

This package contains a diskimage-builder script for creating Octavia Amphora images



%prep
%autosetup -n %{service}-%{upstream_version} -S git

find %{service} -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Let's handle dependencies ourseleves
rm -f requirements.txt
rm -rf octavia.egg-info


%build
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_build}

# Loop through values in octavia-dist.conf and make sure that the values
# are substituted into the octavia.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/%{service}.conf
done < %{SOURCE30}

%install
%{pyver_install}

# Remove unused files
rm -rf %{buildroot}%{pyver_sitelib}/bin
rm -rf %{buildroot}%{pyver_sitelib}/doc
rm -rf %{buildroot}%{pyver_sitelib}/tools

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
export OS_TEST_PATH='./%{service}/tests/unit'
export PATH=$PATH:$RPM_BUILD_ROOT/usr/bin
PYTHON=%{pyver_bin} stestr-%{pyver} run

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

%files -n python%{pyver}-%{service}-tests
%license LICENSE
%{pyver_sitelib}/%{service}/tests

%files -n python%{pyver}-%{service}
%license LICENSE
%{pyver_sitelib}/%{service}
%{pyver_sitelib}/%{service}-*.egg-info
%exclude %{pyver_sitelib}/%{service}/tests


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
%{_bindir}/%{service}-status
%{_bindir}/%{service}-db-manage
%{_bindir}/%{service}-driver-agent

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
* Mon Jun 29 2020 RDO <dev@lists.rdoproject.org> 5.0.2-1
- Update to 5.0.2

* Mon Dec 16 2019 RDO <dev@lists.rdoproject.org> 5.0.1-1
- Update to 5.0.1

* Wed Oct 16 2019 RDO <dev@lists.rdoproject.org> 5.0.0-1
- Update to 5.0.0

* Mon Oct 07 2019 RDO <dev@lists.rdoproject.org> 5.0.0-0.2.0rc2
- Update to 5.0.0.0rc2

* Mon Sep 30 2019 RDO <dev@lists.rdoproject.org> 5.0.0-0.1.0rc1
- Update to 5.0.0.0rc1

