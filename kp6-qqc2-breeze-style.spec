#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.6.0
%define		qtver		5.15.2
%define		kpname		qqc2-breeze-style

Summary:	QQC2StyleBridge
Name:		kp6-%{kpname}
Version:	6.6.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	3d5980a0a36356a9c206fbb053260504
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	kf6-dirs
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	kp5-%{kpname} < 6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style. Unlike
QQC2-Desktop-Style, it does not depend on Qt Widgets and the system
QStyle. It looks like the KDE Visual Design Group's vision for Breeze.

It behaves similar to how the Qt Basic, Fusion and Material QQC2
styles behave, but with various extra features to improve the user
experience.

The performance, loading times and RAM usage should be generally
competitive with the Qt Fusion and Material QQC2 styles.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/qml/org/kde/breeze
%dir %{_libdir}/qt6/qml/org/kde/breeze/impl
%{_libdir}/qt6/qml/org/kde/breeze/impl/ButtonBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/CheckIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/ComboBoxBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/CursorDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/CursorHandle.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/DelegateBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/FocusRect.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/IconLabelContent.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/IconLabelShortcutContent.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/InlineIconLabelContent.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/LargeShadow.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/ListViewHighlight.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/MediumShadow.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/MenuItemBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/OverlayDimBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/OverlayModalBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/RadioIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/ScrollHandle.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/SliderGroove.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/SliderHandle.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/SpinBoxIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/StandardRectangle.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/SwitchIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/TextEditBackground.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/qmldir
%{_libdir}/qt6/qml/org/kde/breeze/qmldir
%{_libdir}/cmake/QQC2BreezeStyle
%{_libdir}/qt6/plugins/kf6/kirigami/platform/org.kde.breeze.so
%{_libdir}/qt6/qml/org/kde/breeze/AbstractButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/ApplicationWindow.qml
%{_libdir}/qt6/qml/org/kde/breeze/BreezeStyle.qmltypes
%{_libdir}/qt6/qml/org/kde/breeze/BusyIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/Button.qml
%{_libdir}/qt6/qml/org/kde/breeze/ButtonGroup.qml
%{_libdir}/qt6/qml/org/kde/breeze/CheckBox.qml
%{_libdir}/qt6/qml/org/kde/breeze/CheckDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/ComboBox.qml
%{_libdir}/qt6/qml/org/kde/breeze/Container.qml
%{_libdir}/qt6/qml/org/kde/breeze/Control.qml
%{_libdir}/qt6/qml/org/kde/breeze/DelayButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/Dial.qml
%{_libdir}/qt6/qml/org/kde/breeze/Dialog.qml
%{_libdir}/qt6/qml/org/kde/breeze/DialogButtonBox.qml
%{_libdir}/qt6/qml/org/kde/breeze/Drawer.qml
%{_libdir}/qt6/qml/org/kde/breeze/Frame.qml
%{_libdir}/qt6/qml/org/kde/breeze/GroupBox.qml
%{_libdir}/qt6/qml/org/kde/breeze/HorizontalHeaderView.qml
%{_libdir}/qt6/qml/org/kde/breeze/ItemDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/Label.qml
%{_libdir}/qt6/qml/org/kde/breeze/Menu.qml
%{_libdir}/qt6/qml/org/kde/breeze/MenuBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/MenuBarItem.qml
%{_libdir}/qt6/qml/org/kde/breeze/MenuItem.qml
%{_libdir}/qt6/qml/org/kde/breeze/MenuSeparator.qml
%{_libdir}/qt6/qml/org/kde/breeze/MobileTextActionsToolBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/Page.qml
%{_libdir}/qt6/qml/org/kde/breeze/PageIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/Pane.qml
%{_libdir}/qt6/qml/org/kde/breeze/Popup.qml
%{_libdir}/qt6/qml/org/kde/breeze/ProgressBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/RadioButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/RadioDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/RangeSlider.qml
%{_libdir}/qt6/qml/org/kde/breeze/RoundButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/ScrollBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/ScrollIndicator.qml
%{_libdir}/qt6/qml/org/kde/breeze/ScrollView.qml
%{_libdir}/qt6/qml/org/kde/breeze/Slider.qml
%{_libdir}/qt6/qml/org/kde/breeze/SpinBox.qml
%{_libdir}/qt6/qml/org/kde/breeze/SplitView.qml
%{_libdir}/qt6/qml/org/kde/breeze/StackView.qml
%{_libdir}/qt6/qml/org/kde/breeze/SwipeDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/SwipeView.qml
%{_libdir}/qt6/qml/org/kde/breeze/Switch.qml
%{_libdir}/qt6/qml/org/kde/breeze/SwitchDelegate.qml
%{_libdir}/qt6/qml/org/kde/breeze/TabBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/TabButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/TextArea.qml
%{_libdir}/qt6/qml/org/kde/breeze/TextField.qml
%{_libdir}/qt6/qml/org/kde/breeze/ToolBar.qml
%{_libdir}/qt6/qml/org/kde/breeze/ToolButton.qml
%{_libdir}/qt6/qml/org/kde/breeze/ToolSeparator.qml
%{_libdir}/qt6/qml/org/kde/breeze/ToolTip.qml
%{_libdir}/qt6/qml/org/kde/breeze/Tumbler.qml
%{_libdir}/qt6/qml/org/kde/breeze/VerticalHeaderView.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/BreezeImpl.qmltypes
%{_libdir}/qt6/qml/org/kde/breeze/impl/SmallBoxShadow.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/Theme.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/Units.qml
%{_libdir}/qt6/qml/org/kde/breeze/impl/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/breeze/impl/libBreezeImpl.so
%{_libdir}/qt6/qml/org/kde/breeze/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/breeze/libBreezeStyle.so
#%{_libdir}/qt6/qml/org/kde/kirigami/styles/org.kde.breeze/AbstractApplicationHeader.qml
