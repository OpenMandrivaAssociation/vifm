Name:           vifm
Version:        0.14.3
Release:        0
Summary:        Ncurses-based file manager with vim-like keybindings
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://%{name}.info
Source0:        https://github.com/vifm/vifm/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  lib64glib2.0-devel
BuildRequires:  groff
BuildRequires:  lib64ncurses-devel
BuildRequires:  desktop-file-utils

%description
Vifm is a ncurses based file manager with vim-like keybindings for managing
your files. 

%prep
%setup -q

%build
%configure \
	--with-curses \
	--with-libmagic \
	--with-glib \
	--disable-developer
%make_build
gzip -9c ChangeLog > ChangeLog.gz

%install
make install DESTDIR="%{?buildroot}"
rm -rf %{buildroot}%{_datadir}/doc/vifm/*
rm -rf %{buildroot}%{_datadir}/vifm/vifmrc-osx
rm -rf %{buildroot}%{_datadir}/vifm/vifm-media-osx
rm -rf %{buildroot}%{_datadir}/vifm/vim-doc/doc/tags
rm -rf %{buildroot}%{_datadir}/vifm/vim-doc/doc/vifm-app.txt

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog.* README TODO
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/vim-doc
%dir %{_datadir}/%{name}/vim-doc/doc
%doc %{_datadir}/%{name}/%{name}-help.txt
%doc %{_datadir}/%{name}/vim-doc/doc/%{name}-lua.txt
%{_bindir}/*
%{_datadir}/%{name}/vim
%{_datadir}/%{name}/%{name}rc
%{_datadir}/%{name}/colors/
%{_datadir}/%{name}/vifm-media
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/vifm
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_vifm
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%{_datadir}/fish/vendor_completions.d/vifm.fish
%dir %{_sysconfdir}/vifm/
%{_sysconfdir}/vifm/colors/
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/128x128/apps/vifm.png
%{_datadir}/icons/hicolor/scalable/apps/vifm.svg

%changelog
