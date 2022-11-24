# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-lyrics

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Music lyrics application
Version:    0.2.0
Release:    1
Group:      Qt/Qt
License:    MIT
URL:        https://scarpino.dev
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-lyrics.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   qml(Amber.Mpris)
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  desktop-file-utils

%description
Music lyrics application.
It does support: ChartLyrics

%if "%{?vendor}" == "chum"
PackageName: Lyrics
Type: desktop-application
DeveloperName: Andrea Scarpino
Categories:
 - Audio
Custom:
  Repo: https://github.com/ilpianista/harbour-Lyrics
Icon: https://github.com/ilpianista/harbour-Lyrics/-/raw/master/icons/harbour-lyrics.svg
Screenshots:
 - https://github.com/ilpianista/harbour-Lyrics/-/raw/master/screenshots/screenshot_1.png
 - https://github.com/ilpianista/harbour-Lyrics/-/raw/master/screenshots/screenshot_2.png
Url:
  Homepage: https://github.com/ilpianista/harbour-Lyrics
  Bugtracker: https://github.com/ilpianista/harbour-Lyrics/-/issues
  Donation: https://paypal.me/andreascarpino
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
