%global tl_name texlogsieve
%global tl_revision 77351
%global tl_bin_links texlogsieve:%{_texmfdistdir}/scripts/texlogsieve/texlogsieve

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6.1
Release:	%{tl_revision}.1
Summary:	Filter and summarize LaTeX log files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/texlogsieve
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogsieve.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlogsieve.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(texlogsieve.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
texlogsieve reads a LaTeX log file (or the standard input if no file is
specified), filters out less relevant messages, and displays a summary
report. It is a texlua script, similar in spirit to tools such as
texfot, texloganalyser, rubber-info, textlog_extract, texlogparser,
texlogfilter, pulp, and others. Highlights: Two reports: the most
important messages from the log file followed by a summary of repeated
messages, undefined references etc.; The program goes to great lengths
to correctly handle TeX line wrapping and does a much better job at that
than existing tools; Multiline messages are treated as a single entity;
Several options to control which messages should be filtered out; No
messages are accidentally removed; The summary report is currently
simple, but useful.

