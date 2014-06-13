%define major	1
%define libname %mklibname guess %{major}
%define devname %mklibname -d guess

Summary:	A high-speed character set detection library
Name:		libguess
Version:	1.1
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://www.atheme.org/project/guess
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libmowgli)

%description
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %{libname}
Group:		System/Libraries
Summary:	A high-speed character set detection library

%description -n %{libname}
Libguess is a high-speed character set detection library. It employs 
discrete-finite automata to deduce the character set of an imput buffer.

%package -n %{devname}
Group:		Development/C
Summary:	A high-speed character set detection library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
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

%files -n %{devname}
%{_libdir}/libguess.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}

