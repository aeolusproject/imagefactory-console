# Generated from image_factory_console-0.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname imagefactory-console
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: QMF Console for Aeolus Image Factory
Name: rubygem-%{gemname}
Version: 0.5.0
Release: 4%{?extra_release}%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://aeolusproject.org

# The source for this packages was pulled from the upstream's git repo.
# Use the following commands to generate the gem
# git clone  git://github.com/aeolusproject/imagefactory-console.git
# cd imagefactory-console
# rake gem
# grab image_factory_console-0.4.0.gem from the pkg subdir
Source0: %{gemname}-%{version}.gem
Requires: rubygems
Requires: ruby(abi) = %{rubyabi}
# These can't be deduced by gem2rpm
Requires: qpid-cpp-client >= 0.8-6
Requires: ruby-qpid-qmf >= 0.8-6
Requires: qpid-qmf >= 0.8-6

BuildRequires: rubygems
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
QMF Console for Aeolus Image Factory


%prep

%build

%install
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}

%files
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Wed Jul 20 2011  Mo Morsi <mmorsi@redhat.com> - 0.4.0-4
- renamed packaged to imagefactory-console

* Wed Jul 20 2011  Mo Morsi <mmorsi@redhat.com> - 0.4.0-3
- remove unused sitelib macro

* Fri Jul 15 2011  Mo Morsi <mmorsi@redhat.com> - 0.4.0-2
- fixes for fedora package compliance

* Thu Jun 16 2011  <jguiditt@redhat.com> - 0.4.0-1
- Add support for push, build and import methods

* Thu Mar 10 2011  <morazi@redhat.com> - 0.2.0-1
- Initial package
