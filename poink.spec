Summary:	Non-suid ping
Summary(pl):	Nie-suidowy ping
Name:		poink
Version:	1.5beta
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://lcamtuf.coredump.cx/soft/%{name}.zip
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sping sends ICMP ECHO requests to network hosts to determine whether
they are alive. It is a small and hopefully secure implementation of
the common ping utility that offers far less control over the packet
options that may be specified (packet size, delay between packets,
etc.), for both security and bandwidth reasons.

%description -l pl
sping wysy�a ��dania ICMP ECHO do host�w w sieci, �eby sprawdzi� czy
�yj�. Jest ma�� i, miejmy nadziej�, bezpieczn� implementacj� znanego
narz�dzia "ping", kt�ra oferuje du�o mniejsz� kontrol� nad
w�asciwo�ciami pakietu kt�re mo�na ustawi� (rozmiar pakietu, przerwy
miedzy pakietami itp.), ze wzgl�du zar�wno na bezpiecze�stwo jak i na
stopie� obci��enia ��cza.

%prep
%setup -q -c -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install poink $RPM_BUILD_ROOT%{_bindir}/ping
install ping.1 $RPM_BUILD_ROOT%{_mandir}/man1/ping.1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%doc *.gz
