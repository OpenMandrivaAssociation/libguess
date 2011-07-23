%define name libguess
%define version 1.0
%define release %mkrel 2
%define major 1
%define libname %mklibname guess %major
%define develname %mklibname -d guess
Summary: A high-speed character set detection library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://mirror.billymays.us/%name/%{name}-%{version}.tgz
License: BSD
Group: System/Libraries
Url: http://www.atheme.org/project/guess
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libmowgli-devel >= 0.7.0

%description
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %libname
Group: System/Libraries
Summary: A high-speed character set detection library

%description -n %libname
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %develname
Group: Development/C
Summary: A high-speed character set detection library
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

Install this if you want to build applications with %name.

%prep
%setup -q -n %name-%version

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%doc README COPYING
%_libdir/libguess.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libguess.so
%_libdir/pkgconfig/%name.pc
%_includedir/%name
