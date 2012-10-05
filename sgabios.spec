Name:           sgabios
Version:        0
Release:        %mkrel 0.svn.20110622
Summary:        Open-source serial graphics BIOS option rom

Group:          Emulators
License:        ASL 2.0
URL:            http://code.google.com/p/sgabios/
# Tarball created from SVN archive using the following commands:
# svn export -r 8 http://sgabios.googlecode.com/svn/trunk sgabios-0
# tar -czvf sgabios-0-svnr8.tar.gz sgabios-0
Source0:        sgabios-0-svnr8.tar.gz

ExclusiveArch: %{ix86} x86_64

Requires: %{name}-bin = %{version}-%{release}

# Sgabios is noarch, but required on architectures which cannot build it.
# Disable debuginfo because it is of no use to us.
%global debug_package %{nil}

%description
SGABIOS is designed to be inserted into a BIOS as an option rom to provide over
a serial port the display and input capabilities normally handled by a VGA
adapter and a keyboard, and additionally provide hooks for logging displayed
characters for later collection after an operating system boots.

%ifarch %{ix86} x86_64 
%package bin
Summary: Sgabios for x86
Buildarch: noarch

%description bin
SGABIOS is designed to be inserted into a BIOS as an option rom to provide over 
a serial port the display and input capabilities normally handled by a VGA
adapter and a keyboard, and additionally provide hooks for logging displayed
characters for later collection after an operating system boots.
%endif

%prep
%setup -q

%build
mkdir -p bfd
ln -s %{_bindir}/ld.bfd bfd/ld
export PATH=$PWD/bfd:$PATH
unset MAKEFLAGS
%ifarch %{ix86} x86_64 
export CFLAGS="$RPM_OPT_FLAGS"
make
%endif


%install
mkdir -p %{buildroot}%{_datadir}/sgabios
%ifarch %{ix86} x86_64 
install -m 0644 sgabios.bin %{buildroot}%{_datadir}/sgabios
%endif


%files
%doc COPYING design.txt

%ifarch %{ix86} x86_64 
%files bin
%dir %{_datadir}/sgabios/
%{_datadir}/sgabios/sgabios.bin
%endif
