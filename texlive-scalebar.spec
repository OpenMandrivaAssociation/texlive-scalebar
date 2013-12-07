# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/scalebar
# catalog-date 2006-11-06 13:28:58 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-scalebar
Version:	1.0
Release:	5
Summary:	Create scalebars for maps, diagrams or photos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scalebar
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scalebar.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755797
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719488
- texlive-scalebar
- texlive-scalebar
- texlive-scalebar
- texlive-scalebar

