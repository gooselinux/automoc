%global beta 0.9.88
%global beta_tag rc3

Name: automoc
Version: 1.0
Release: 0.14.%{?beta_tag}%{?dist}
Summary: Automatic moc for Qt 4
Group: Development/Tools
License: BSD
URL: http://www.kde.org
Source0: ftp://ftp.kde.org/pub/kde/stable/automoc4/%{beta}/automoc4-%{beta}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: automoc4 = %{beta}

Requires: cmake >= 2.4.5

BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel
BuildRequires: kde-filesystem

%description
This package contains the automoc4 binary which is used to run moc on the
right source files in a Qt 4 or KDE 4 application.
Moc is the meta object compiler which is a widely used tool with Qt and
creates standard C++ files to provide syntactic sugar of the signal/slots
mechanism.


%prep
%setup -q -n automoc4-%{beta}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/automoc4
%{_kde4_libdir}/automoc4/


%changelog
* Tue Mar 30 2010 Than Ngo <than@redhat.com> - 1.0-0.14.rc3
- rebuilt against qt 4.6.2

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-0.13.rc3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.13.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.12.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Rex Dieter <rdieter@fedoraproject.org> 1.0-0.11.rc3
- automoc4-0.9.88 (1.0-rc3)

* Sat Nov 22 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.10.rc2
- fix package summary and descriptions (as requested by Richard Hughes)
- match cmake minimum required version with the contents of CMakeLists.txt
  (paranoid fix)

* Thu Sep  4 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.9.rc2
- automoc4-0.9.87 (1.0-rc2)

* Wed Jul 23 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0-0.8.rc1
- automoc4-0.9.84 (1.0-rc1)

* Mon Jun 30 2008 Rex Dieter <rdieter@fedoraproject.org> 1.0-0.7.beta2
- automoc4-0.9.83 (1.0-beta2)
- drop lib64 patch

* Thu Jun 10 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.5.20080527svn811390
- Leave automoc4.files.in in _libdir
- Same applies to Automoc4Config.cmake

* Thu May 29 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.3.20080527svn811390
- Added 'cmake' to Requires

* Wed May 28 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.2.20080527svn811390
- Patched to make it build on other systems than i386 (thanks to Rex Dieter)

* Tue May 27 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 1.0-0.1.20080527svn811390
- Initial release
