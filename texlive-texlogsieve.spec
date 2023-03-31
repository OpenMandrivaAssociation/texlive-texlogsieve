Name:		texlive-texlogsieve
Version:	64301
Release:	2
Summary:	Filter and summarize LaTeX log files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texlogsieve
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogsieve.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogsieve.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
texlogsieve reads a LaTeX log file (or the standard input if no
file is specified), filters out less relevant messages, and
displays a summary report. It is a texlua script, similar in
spirit to tools such as texfot, texloganalyser, rubber-info,
textlog_extract, texlogparser, and others. Highlights: Two
reports: the most important messages from the log file followed
by a summary of repeated messages, undefined references etc.;
The program goes to great lengths to correctly handle TeX line
wrapping and does a much better job at that than existing
tools; Multiline messages are treated as a single entity;
Several options to control which messages should be filtered
out; No messages are accidentally removed; The summary report
is currently simple, but useful.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/texlogsieve
%doc %{_texmfdistdir}/texmf-dist/doc/support/texlogsieve
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlogsieve.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/texlogsieve.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
