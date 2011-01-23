# TODO
# - build from src
%include	/usr/lib/rpm/macros.java
Summary:	Small footprint Dependency Injection container
Summary(pl.UTF-8):	Kontener Dependency Injection o małym narzucie
Name:		picocontainer
Version:	1.3
Release:	0.1
License:	PicoContainer
Group:		Development/Languages/Java
#Source0:	http://repository.codehaus.org/org/picocontainer/picocontainer-distribution/1.3/picocontainer-distribution-1.3-src.zip
Source0:	http://repository.codehaus.org/org/picocontainer/picocontainer/1.3/%{name}-%{version}-javadoc.jar
# Source0-md5:	0da41a3757fde313d4baedd63d29e35d
Source1:	http://repository.codehaus.org/org/picocontainer/picocontainer/1.3/%{name}-%{version}.jar
# Source1-md5:	2f3dfbc6e1273c95d9d9ecb4b74bec50
URL:		http://www.picocontainer.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PicoContainer is a lightweight and highly embeddable container for
components that honour Dependency Injection.

%description -l pl.UTF-8
PicoContainer to lekki i dobrze osadzalny kontener dla komponentów
honorujących Dependency Injection.

%package javadoc
Summary:	Online manual for %{name}
Summary(pl.UTF-8):	Dokumentacja online do %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
# install jar
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a . $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
