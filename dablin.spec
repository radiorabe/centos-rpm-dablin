Name:     dablin

Version:  master
Release:  1
Summary:  DAB/DAB+ receiver for Linux (including ETI-NI playback)
License:  GPLv3+
URL:      https://github.com/Opendigitalradio/dablin
Source0:  https://github.com/Opendigitalradio/dablin/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:   dablin-fdk-aac.patch

BuildRequires: gcc-c++
BuildRequires: libfec-odr-devel
BuildRequires: fdk-aac-dabplus-odr
BuildRequires: libmpg123-devel
BuildRequires: faad2-devel
BuildRequires: SDL2-devel
BuildRequires: gtkmm30-devel

%description
DABlin plays a DAB/DAB+ audio service - either from a received live transmission or
from a stored ensemble recording (frame-aligned ETI-NI). Both DAB (MP2) and DAB+ 
(AAC-LC, HE-AAC, HE-AAC v2) services are supported.

%package -n dablin-gtk
Summary:  DAB/DAB+ receiver for Linux/GTK (including ETI-NI playback)
Requires: %{name} = %{version}-%{release}

%description -n dablin-gtk
DABlin plays a DAB/DAB+ audio service - either from a received live transmission or
from a stored ensemble recording (frame-aligned ETI-NI). Both DAB (MP2) and DAB+ 
(AAC-LC, HE-AAC, HE-AAC v2) services are supported.


%prep
%setup -q
%patch0

%build
make

%install
install -d %{buildroot}/usr/bin/
install dablin %{buildroot}/usr/bin/
install dablin_gtk %{buildroot}/usr/bin/

%files
%doc README.md COPYING
%{_bindir}/dablin

%files -n dablin-gtk
%{_bindir}/dablin_gtk
