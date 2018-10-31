# revision 33888
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langeuropean
Version:	20180304
Release:	2
Summary:	Other European languages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langeuropean.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-armtex
Requires:	texlive-babel-albanian
Requires:	texlive-babel-breton
Requires:	texlive-babel-croatian
Requires:	texlive-babel-danish
Requires:	texlive-babel-dutch
Requires:	texlive-babel-estonian
Requires:	texlive-babel-finnish
Requires:	texlive-babel-friulan
Requires:	texlive-babel-hungarian
Requires:	texlive-babel-icelandic
Requires:	texlive-babel-irish
Requires:	texlive-babel-kurmanji
Requires:	texlive-babel-latin
Requires:	texlive-babel-norsk
Requires:	texlive-babel-piedmontese
Requires:	texlive-babel-romanian
Requires:	texlive-babel-romansh
Requires:	texlive-babel-samin
Requires:	texlive-babel-scottish
Requires:	texlive-babel-slovenian
Requires:	texlive-babel-swedish
Requires:	texlive-babel-turkish
Requires:	texlive-babel-welsh
Requires:	texlive-finbib
Requires:	texlive-hrlatex
Requires:	texlive-hyphen-armenian
Requires:	texlive-hyphen-croatian
Requires:	texlive-hyphen-danish
Requires:	texlive-hyphen-dutch
Requires:	texlive-hyphen-estonian
Requires:	texlive-hyphen-finnish
Requires:	texlive-hyphen-friulan
Requires:	texlive-hyphen-hungarian
Requires:	texlive-hyphen-icelandic
Requires:	texlive-hyphen-irish
Requires:	texlive-hyphen-kurmanji
Requires:	texlive-hyphen-latin
Requires:	texlive-hyphen-latvian
Requires:	texlive-hyphen-lithuanian
Requires:	texlive-hyphen-norwegian
Requires:	texlive-hyphen-piedmontese
Requires:	texlive-hyphen-romanian
Requires:	texlive-hyphen-romansh
Requires:	texlive-hyphen-slovenian
Requires:	texlive-hyphen-swedish
Requires:	texlive-hyphen-turkish
Requires:	texlive-hyphen-uppersorbian
Requires:	texlive-hyphen-welsh
Requires:	texlive-lithuanian
Requires:	texlive-lshort-dutch
Requires:	texlive-lshort-finnish
Requires:	texlive-lshort-slovenian
Requires:	texlive-lshort-turkish
Requires:	texlive-swebib
Requires:	texlive-turkmen

%description
Support for a number of European languages; others (Greek,
German, French, ...) have their own collections, depending
simply on the size of the support.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
