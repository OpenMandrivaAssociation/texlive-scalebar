Name:		texlive-scalebar
Version:	15878
Release:	1
Summary:	Create scalebars for maps, diagrams or photos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scalebar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small package to create scalebars for maps, diagrams
or photos. It was designed for use with cave maps but can be
used for anything from showing a scalebar in kilometers for
topographic maps to a scalebar in micrometers for an electron
microscope image.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/scalebar/scalebar.sty
%doc %{_texmfdistdir}/doc/latex/scalebar/README
%doc %{_texmfdistdir}/doc/latex/scalebar/scalebar_examples.pdf
%doc %{_texmfdistdir}/doc/latex/scalebar/scalebar_examples.tex
#- source
%doc %{_texmfdistdir}/source/latex/scalebar/scalebar.dtx
%doc %{_texmfdistdir}/source/latex/scalebar/scalebar.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
