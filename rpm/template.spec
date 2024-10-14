%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-ur-calibration
Version:        2.4.12
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_calibration package

License:        BSD-3-Clause
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-rolling-rclcpp
Requires:       ros-rolling-ur-client-library
Requires:       ros-rolling-ur-robot-driver
Requires:       yaml-cpp-devel
Requires:       ros-rolling-ros-workspace
BuildRequires:  eigen3-devel
BuildRequires:  ros-rolling-ament-cmake
BuildRequires:  ros-rolling-rclcpp
BuildRequires:  ros-rolling-ur-client-library
BuildRequires:  ros-rolling-ur-robot-driver
BuildRequires:  yaml-cpp-devel
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-rolling-ament-cmake-gmock
BuildRequires:  ros-rolling-ament-cmake-gtest
BuildRequires:  ros-rolling-ament-lint-auto
BuildRequires:  ros-rolling-ament-lint-common
%endif

%description
Package for extracting the factory calibration from a UR robot and change it
such that it can be used by ur_description to gain a correct URDF

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DAMENT_PREFIX_PATH="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Mon Oct 14 2024 Felix Exner <exner@fzi.de> - 2.4.12-1
- Autogenerated by Bloom

* Fri Oct 11 2024 Felix Exner <exner@fzi.de> - 2.4.11-1
- Autogenerated by Bloom

* Thu Sep 12 2024 Felix Exner <exner@fzi.de> - 2.4.10-1
- Autogenerated by Bloom

* Sun Aug 11 2024 Felix Exner <exner@fzi.de> - 2.4.9-1
- Autogenerated by Bloom

* Mon Jul 01 2024 Felix Exner <exner@fzi.de> - 2.4.8-1
- Autogenerated by Bloom

* Thu Jun 20 2024 Felix Exner <exner@fzi.de> - 2.4.7-1
- Autogenerated by Bloom

* Mon Jun 17 2024 Felix Exner <exner@fzi.de> - 2.4.6-1
- Autogenerated by Bloom

* Sat May 18 2024 Felix Exner <exner@fzi.de> - 2.4.5-1
- Autogenerated by Bloom

