# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/scalebar
# catalog-date 2006-11-06 13:28:58 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-scalebar
Version:	1.0
Release:	1
Summary:	Create scalebars for maps, diagrams or photos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scalebar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a small package to create scalebars for maps, diagrams
or photos. It was designed for use with cave maps but can be
used for anything from showing a scalebar in kilometers for
topographic maps to a scalebar in micrometers for an electron
microscope image.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
