# TODO:
# - type1 fonts also available in zip archive
# - create -installer if wanted to include in distro
Summary:	Mathematica fonts from Wolfram Research, Inc.
Summary(pl.UTF-8):	Fonty dla programu Mathematica produkcji Wolfram Research, Inc.
Name:		fonts-TTF-MathFonts
Version:	5.2
Release:	1
License:	restricted, see URL
Group:		Fonts
Source0:	http://support.wolfram.com/mathematica/systems/windows/general/files/MathFonts_%{version}.zip
# NoSource0-md5:	2f6898c0b0848b3faad21873d8fd1f9f
NoSource:	0
Source1:	%{name}-license.txt
URL:		http://support.wolfram.com/mathematica/systems/windows/general/latestfonts.html
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description
The TrueType font packs are provided by Wolfram Research, Inc.

%description -l pl.UTF-8
Fonty dla programu Mathematica produkcji Wolfram Research, Inc.

%prep
%setup -qc
cp %{SOURCE1} license.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}
cp -a Fonts/TrueType/*.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc license.txt
%{ttffontsdir}/*.ttf
