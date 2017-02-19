#
# spec file for package dablin and subpackage dablin-gtk
#
# Copyright (c) 2016 - 2017 Radio Bern RaBe
#                           http://www.rabe.ch
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public 
# License as published  by the Free Software Foundation, version
# 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License  along with this program.
# If not, see <http://www.gnu.org/licenses/>.
#
# Please submit enhancements, bugfixes or comments via GitHub:
# https://github.com/radiorabe/centos-rpm-dablin
#

Name:     dablin

Version:  1.3.0
Release:  2%{?dist}
Summary:  DAB/DAB+ receiver for Linux (including ETI-NI playback)
# The entire source code is GPLv3+ except fec/ which is LGPLv2.1+
License:  GPLv3+ and LGPLv2.1+
URL:      https://github.com/Opendigitalradio/dablin
Source0:  https://github.com/Opendigitalradio/dablin/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: faad2-devel
BuildRequires: libmpg123-devel >= 1.14.0
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

%build
%cmake .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README.md COPYING
%{_bindir}/dablin

%files -n dablin-gtk
%{_bindir}/dablin_gtk


%changelog
* Sun Feb 19 2017 Christian Affolter <c.affolter@purplehaze.ch> - 1.3.0-2
- Bump to upstream version 1.3.0
- Switched to cmake
- Removed libfec dependency, which is bundled now

* Sat Jan 28 2017 Christian Affolter <c.affolter@purplehaze.ch> - 1.2.0-1
- Bump to upstream version 1.2.0

* Sat Oct 22 2016 Lucas Bickel <hairmare@purplehaze.ch> - 1.1.0-1
- Bump to upstream version 1.1.0
- Use faad2 aac decoder instead of fdk-aac-dabplus-odr

* Wed Sep 28 2016 Lucas Bickel <hairmare@purplehaze.ch> - 1.0.0-2
- Adapted to accommodate changes to upstream fdk-aac-dabplus-odr package

* Thu Aug 25 2016 Christian Affolter <c.affolter@purplehaze.ch> - 1.0.0-1
- Switched from Git master to first upstream release
- Adapted build dependency, to match the new name of libfdk-aac-dabplus-odr-devel

* Sun Aug 21 2016 Christian Affolter <c.affolter@purplehaze.ch> - master-2
- Switched to libfdk-dabplus-odr (FDK AAC Codec from Opendigitalradio)

* Sun Aug 21 2016 Lucas Bickel <hairmare@purplehaze.ch> - master-1
- Initial release
