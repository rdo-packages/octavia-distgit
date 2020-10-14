%global milestone .0rc1
%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service octavia
%global common_desc Octavia is an Operator-grade open source scalable load balancer.

Name:       openstack-%{service}
Version:    7.0.0
Release:    0.1%{?milestone}%{?dist}
Summary:    Octavia, a load balancer implementation for OpenStack

License:    ASL 2.0
URL:        http://launchpad.net/%{service}/

Source0:    https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz
#
# patches_base=7.0.0.0rc1
#

Source1:    %{service}.logrotate
Source10:   %{service}-amphora-agent.service
Source11:   %{service}-api.service
Source12:   %{service}-worker.service
Source13:   %{service}-health-manager.service
Source14:   %{service}-housekeeping.service

Source30:   %{service}-dist.conf
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  systemd
BuildRequires:  openstack-macros
BuildRequires:  git

# BuildRequires for running functional tests
BuildRequires:  python3-stestr
BuildRequires:  python3-mock
BuildRequires:  python3-subunit
BuildRequires:  python3-oslotest
BuildRequires:  python3-testrepository
BuildRequires:  python3-testtools
BuildRequires:  python3-testresources
BuildRequires:  python3-testscenarios
BuildRequires:  python3-oslo-utils
BuildRequires:  python3-oslo-upgradecheck
BuildRequires:  python3-flask
BuildRequires:  python3-oslo-config
BuildRequires:  python3-oslo-log
BuildRequires:  python3-glanceclient
BuildRequires:  python3-wsme
BuildRequires:  python3-barbicanclient
BuildRequires:  python3-cryptography
BuildRequires:  python3-gunicorn
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-netaddr
BuildRequires:  python3-novaclient
BuildRequires:  python3-taskflow
BuildRequires:  python3-neutronclient
BuildRequires:  python3-oslo-db
BuildRequires:  python3-oslo-reports
BuildRequires:  python3-oslo-policy
BuildRequires:  python3-pecan
BuildRequires:  python3-pyroute2
BuildRequires:  python3-pyasn1
BuildRequires:  python3-oslo-messaging
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-cotyledon
BuildRequires:  python3-keystonemiddleware
BuildRequires:  python3-werkzeug
BuildRequires:  python3-distro
BuildRequires:  python3-castellan
BuildRequires:  python3-octavia-lib >= 1.3.1
BuildRequires:  python3-debtcollector
BuildRequires:  python3-cinderclient
BuildRequires:  python3-sqlalchemy-utils
BuildRequires:  python3-requests-mock
BuildRequires:  python3-netifaces

Requires:   python3-%{service} = %{version}-%{release}

Requires(pre): shadow-utils
%if 0%{?rhel} && 0%{?rhel} < 8
%{?systemd_requires}
%else
%{?systemd_ordering} # does not exist on EL7
%endif

%description
%{common_desc}


%package -n python3-%{service}
Summary:    Octavia Python libraries
%{?python_provide:%python_provide python3-%{service}}
Group:      Applications/System


Requires:   python3-alembic >= 0.8.10
Requires:   python3-pecan >= 1.3.2
Requires:   python3-pbr >= 2.0.0
Requires:   python3-sqlalchemy >= 1.2.19
Requires:   python3-babel >= 2.3.4
Requires:   python3-requests >= 2.14.2
Requires:   python3-keystonemiddleware >= 4.17.0
Requires:   python3-netaddr >= 0.7.19
Requires:   python3-neutronclient >= 6.7.0
Requires:   python3-webob >= 1.8.2
Requires:   python3-stevedore >= 1.20.0
Requires:   python3-oslo-config >= 2:5.2.0
Requires:   python3-oslo-context >= 2.19.2
Requires:   python3-oslo-db >= 8.3.0
Requires:   python3-oslo-i18n >= 3.15.3
Requires:   python3-oslo-serialization >= 2.18.0
Requires:   python3-oslo-log >= 3.36.0
Requires:   python3-oslo-messaging >= 12.4.0
Requires:   python3-oslo-middleware >= 4.0.1
Requires:   python3-oslo-policy >= 1.30.0
Requires:   python3-oslo-utils >= 3.33.0
Requires:   python3-oslo-upgradecheck >= 0.1.0
Requires:   python3-barbicanclient >= 4.5.2
Requires:   python3-novaclient >= 1:9.1.0
Requires:   python3-pyOpenSSL >= 18.0.0
Requires:   python3-wsme >= 0.8.0
Requires:   python3-pyasn1 >= 0.1.8
Requires:   python3-pyasn1-modules >= 0.0.6
Requires:   python3-jinja2 >= 2.10
Requires:   python3-taskflow >= 4.4.0
Requires:   python3-flask >= 0.10
Requires:   python3-cryptography >= 2.8
Requires:   python3-keystoneauth1 >= 3.4.0
Requires:   python3-oslo-reports >= 1.18.0
Requires:   python3-glanceclient >= 1:2.8.0
Requires:   python3-rfc3986 >= 0.3.1
Requires:   python3-pyroute2 >= 0.5.13
Requires:   python3-gunicorn >= 19.9.0
Requires:   python3-cotyledon >= 1.3.0
Requires:   python3-werkzeug >= 0.14.1
Requires:   python3-distro >= 1.2.0
Requires:   python3-castellan >= 0.16.0
Requires:   python3-PyMySQL >= 0.8.0
Requires:   python3-futurist >= 1.2.0
Requires:   python3-tenacity >= 5.0.4
Requires:   python3-octavia-lib >= 2.2.0
Requires:   python3-jsonschema >= 3.2.0
Requires:   python3-cinderclient >= 3.3.0
Requires:   python3-setproctitle >= 1.1.10
Requires:   python3-simplejson >= 3.13.2
Requires:   python3-sqlalchemy-utils >= 0.30.11
Requires:   python3-netifaces >= 0.10.4


%description -n python3-%{service}
%{common_desc}

This package contains the Octavia Python library.

%package -n python3-%{service}-tests
Summary:    Octavia tests
%{?python_provide:%python_provide python3-%{service}-tests}
Group:      Applications/System

Requires:   python3-%{service} = %{version}-%{release}

Requires:   python3-mock
Requires:   python3-subunit
Requires:   python3-oslotest
Requires:   python3-testrepository
Requires:   python3-testtools
Requires:   python3-testresources
Requires:   python3-testscenarios
Requires:   python3-tempest

Requires:   python3-requests-mock

%description -n python3-%{service}-tests
%{common_desc}

This package contains Octavia test files.

%package common
Summary:    Octavia common files
Group:      Applications/System

Requires:   python3-%{service} = %{version}-%{release}


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
Requires:   diskimage-builder >= 2.24.0


%description diskimage-create
%{common_desc}

This package contains a diskimage-builder script for creating Octavia Amphora images



%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{service}-%{upstream_version} -S git

find %{service} -name \*.py -exec sed -i '/\/usr\/bin\/env python/{d;q}' {} +

# Let's handle dependencies ourseleves
rm -f requirements.txt
rm -rf octavia.egg-info


%build
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{py3_build}

# Loop through values in octavia-dist.conf and make sure that the values
# are substituted into the octavia.conf as comments. Some of these values
# will have been uncommented as a way of upstream setting defaults outside
# of the code.
while read name eq value; do
  test "$name" && test "$value" || continue
  sed -ri "0,/^(#)? *$name *=/{s!^(#)? *$name *=.*!# $name = $value!}" etc/%{service}.conf
done < %{SOURCE30}

%install
%{py3_install}

# Remove unused files
rm -rf %{buildroot}%{python3_sitelib}/bin
rm -rf %{buildroot}%{python3_sitelib}/doc
rm -rf %{buildroot}%{python3_sitelib}/tools

# Move config files to proper location
install -d -m 755 %{buildroot}%{_sysconfdir}/%{service}
mv %{buildroot}/usr/etc/%{service}/%{service}.conf %{buildroot}%{_sysconfdir}/%{service}

# Move policy.yaml to proper location
mv etc/policy/admin_or_owner-policy.yaml %{buildroot}%{_sysconfdir}/%{service}/policy.yaml

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
# We do not want to run linter checks here
rm -f octavia/tests/unit/test_hacking.py
# Skip test until issue created by https://review.opendev.org/#/c/697128/ is fixed
PYTHON=%{__python3} stestr run --black-regex 'test_cmd_get_version_of_installed_package_mapped'

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

%files -n python3-%{service}-tests
%license LICENSE
%{python3_sitelib}/%{service}/tests

%files -n python3-%{service}
%license LICENSE
%{python3_sitelib}/%{service}
%{python3_sitelib}/%{service}-*.egg-info
%exclude %{python3_sitelib}/%{service}/tests


%files common
%license LICENSE
%doc README.rst
%dir %{_sysconfdir}/%{service}/conf.d
%dir %{_sysconfdir}/%{service}/conf.d/common
%attr(-, root, %{service}) %{_datadir}/%{service}/%{service}-dist.conf
%config(noreplace) %attr(0640, root, %{service}) %{_sysconfdir}/%{service}/%{service}.conf
%config(noreplace) %attr(0640, root, %{service}) %{_sysconfdir}/%{service}/policy.yaml
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
* Wed Oct 14 2020 Joel Capitao <jcapitao@redhat.com> 7.0.0-0.1.0rc1
- Enable sources tarball validation using GPG signature.

* Fri Sep 25 2020 RDO <dev@lists.rdoproject.org> 7.0.0-0.1.0rc1
- Update to 7.0.0.0rc1

