%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ur-moveit-config
Version:        2.2.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ur_moveit_config package

License:        Apache2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-launch
Requires:       ros-humble-launch-ros
Requires:       ros-humble-moveit-kinematics
Requires:       ros-humble-moveit-planners-ompl
Requires:       ros-humble-moveit-ros-move-group
Requires:       ros-humble-moveit-ros-visualization
Requires:       ros-humble-moveit-servo
Requires:       ros-humble-moveit-simple-controller-manager
Requires:       ros-humble-rviz2
Requires:       ros-humble-ur-description
Requires:       ros-humble-urdf
Requires:       ros-humble-warehouse-ros-sqlite
Requires:       ros-humble-xacro
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-cmake-python
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
An example package with MoveIt2 configurations for UR robots.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
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
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Nov 22 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.5-1
- Autogenerated by Bloom

* Fri Oct 07 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.4-1
- Autogenerated by Bloom

* Mon Aug 01 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.3-1
- Autogenerated by Bloom

* Tue Jul 19 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.2-1
- Autogenerated by Bloom

* Mon Jun 27 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.1-1
- Autogenerated by Bloom

* Tue Jun 21 2022 Denis Stogl <denis@stoglrobotics.de> - 2.2.0-1
- Autogenerated by Bloom

