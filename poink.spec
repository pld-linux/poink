Summary:	Non-suid ping
Summary(pl):	Nie-suidowy ping
Name:		poink
Version:	2.03
Release:	3
License:	GPL v2
Group:		Networking/Admin
Source0:	http://ep09.pld-linux.org/~mmazur/%{name}/files/%{name}-%{version}.tar.gz
# Source0-md5:	c04cc09b88937730deb0ebe06eb988a0
URL:		http://ep09.pld-linux.org/~mmazur/poink/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Poink sends TCP linear syn/rst challenges to network hosts to
determine whether they are alive. It is a small and hopefully secure
implementation of the common ping utility that offers far less control
over the packet options that may be specified (packet size, delay
between packets, etc.), for both security and bandwidth reasons.

%description -l pl
Poink wysy³a linearne wyzwania syn/rst do hostów w sieci, ¿eby
sprawdziæ czy ¿yj±. Jest ma³± i, miejmy nadziejê, bezpieczn±
implementacj± znanego narzêdzia "ping", która oferuje du¿o mniejsz±
kontrolê nad w³a¶ciwo¶ciami pakietu które mo¿na ustawiæ (rozmiar
pakietu, przerwy miedzy pakietami itp.), ze wzglêdu zarówno na
bezpieczeñstwo jak i na stopieñ obci±¿enia ³±cza.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%doc README ChangeLog
