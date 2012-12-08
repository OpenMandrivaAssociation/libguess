%define major 1
%define libname %mklibname guess %{major}
%define develname %mklibname -d guess

Summary:	A high-speed character set detection library
Name:		libguess
Version:	1.1
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/project/guess
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2
BuildRequires:	libmowgli-devel >= 0.7.0

%description
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %{libname}
Group:		System/Libraries
Summary:	A high-speed character set detection library

%description -n %{libname}
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %{develname}
Group:		Development/C
Summary:	A high-speed character set detection library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

Install this if you want to build applications with %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libguess.so.%{major}*

%files -n %{develname}
%{_libdir}/libguess.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}


%changelog
* Fri Dec 02 2011 Götz Waschk <waschk@mandriva.org> 1.1-1mdv2012.0
+ Revision: 737133
- new version
- update source URL

* Sat Jul 23 2011 Götz Waschk <waschk@mandriva.org> 1.0-2
+ Revision: 691242
- rebuild

* Thu Jul 22 2010 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2011.0
+ Revision: 556861
- import libguess


