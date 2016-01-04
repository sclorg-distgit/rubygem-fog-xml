%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from fog-xml-0.1.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-xml

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.1
Release: 3%{?dist}
Summary: XML parsing for fog providers
Group: Development/Languages
License: MIT
URL: https://github.com/fog/fog-xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix}rubygem(fog-core)
Requires: %{?scl_prefix}rubygem(nokogiri) => 1.5.11
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix}rubygem(fog-core)
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix}rubygem(nokogiri)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Extraction of the XML parsing tools shared between a
number of providers in the 'fog' gem.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# We don't have Turn in Fedora (neither we really need it).
sed -i '/require.*turn/ s/^/#/' spec/minitest_helper.rb
sed -i '/Turn/,/end/ s/^/#/' spec/minitest_helper.rb

%{?scl:scl enable %{scl} - << \EOF}
ruby -Ilib:spec -e 'Dir.glob "./spec/**/*_spec.rb", &method(:require)'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.md
%exclude %{gem_instdir}/fog-xml.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gemfiles
%{gem_instdir}/spec

%changelog
* Fri Jun 12 2015 Josef Stribny <jstribny@redhat.com> - 0.1.1-3
- Add missing provide

* Fri Jun 05 2015 Josef Stribny <jstribny@redhat.com> - 0.1.1-2
- Add SCL macros

* Tue Mar 10 2015 Vít Ondruch <vondruch@redhat.com> - 0.1.1-1
- Initial package
