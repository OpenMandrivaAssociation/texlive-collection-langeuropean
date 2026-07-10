%global tl_name collection-langeuropean
%global tl_revision 79350

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Other European languages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langeuropean
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langeuropean.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(armtex)
Requires:	texlive(babel-albanian)
Requires:	texlive(babel-bosnian)
Requires:	texlive(babel-breton)
Requires:	texlive(babel-croatian)
Requires:	texlive(babel-danish)
Requires:	texlive(babel-dutch)
Requires:	texlive(babel-estonian)
Requires:	texlive(babel-finnish)
Requires:	texlive(babel-friulan)
Requires:	texlive(babel-hungarian)
Requires:	texlive(babel-icelandic)
Requires:	texlive(babel-irish)
Requires:	texlive(babel-kurmanji)
Requires:	texlive(babel-latin)
Requires:	texlive(babel-latvian)
Requires:	texlive(babel-lithuanian)
Requires:	texlive(babel-macedonian)
Requires:	texlive(babel-norsk)
Requires:	texlive(babel-occitan)
Requires:	texlive(babel-piedmontese)
Requires:	texlive(babel-romanian)
Requires:	texlive(babel-romansh)
Requires:	texlive(babel-samin)
Requires:	texlive(babel-scottish)
Requires:	texlive(babel-slovenian)
Requires:	texlive(babel-swedish)
Requires:	texlive(babel-turkish)
Requires:	texlive(babel-welsh)
Requires:	texlive(collection-basic)
Requires:	texlive(finbib)
Requires:	texlive(gloss-occitan)
Requires:	texlive(hrlatex)
Requires:	texlive(huaz)
Requires:	texlive(hulipsum)
Requires:	texlive(hyphen-albanian)
Requires:	texlive(hyphen-croatian)
Requires:	texlive(hyphen-danish)
Requires:	texlive(hyphen-dutch)
Requires:	texlive(hyphen-estonian)
Requires:	texlive(hyphen-finnish)
Requires:	texlive(hyphen-friulan)
Requires:	texlive(hyphen-hungarian)
Requires:	texlive(hyphen-icelandic)
Requires:	texlive(hyphen-irish)
Requires:	texlive(hyphen-kurmanji)
Requires:	texlive(hyphen-latin)
Requires:	texlive(hyphen-latvian)
Requires:	texlive(hyphen-lithuanian)
Requires:	texlive(hyphen-macedonian)
Requires:	texlive(hyphen-norwegian)
Requires:	texlive(hyphen-occitan)
Requires:	texlive(hyphen-piedmontese)
Requires:	texlive(hyphen-romanian)
Requires:	texlive(hyphen-romansh)
Requires:	texlive(hyphen-slovenian)
Requires:	texlive(hyphen-swedish)
Requires:	texlive(hyphen-turkish)
Requires:	texlive(hyphen-uppersorbian)
Requires:	texlive(hyphen-welsh)
Requires:	texlive(kaytannollista-latexia)
Requires:	texlive(lithuanian)
Requires:	texlive(lshort-dutch)
Requires:	texlive(lshort-estonian)
Requires:	texlive(lshort-finnish)
Requires:	texlive(lshort-slovenian)
Requires:	texlive(lshort-turkish)
Requires:	texlive(nevelok)
Requires:	texlive(rojud)
Requires:	texlive(swebib)
Requires:	texlive(turkce-sayi)
Requires:	texlive(turkmen)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for a number of European languages; others (Greek, German,
French, ...) have their own collections, depending simply on the size of
the support.

