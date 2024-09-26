cmake_minimum_required(VERSION 3.5)
project(lab1_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)  # Corrected from "rclpp" to "rclcpp"
find_package(rclpy REQUIRED)

include_directories(include)

# Create cpp executables
add_executable(cpp_exe src/cpp_node.cpp)
ament_target_dependencies(cpp_exe rclcpp)

# Install cpp executables
install(TARGETS
  cpp_exe
  DESTINATION lib/${PROJECT_NAME}
)

# Install Py modules
ament_python_install_package(${PROJECT_NAME})

# Install Py executables (Add talker.py and relay.py)
install(PROGRAMS
  scripts/py_node.py
  scripts/talker.py       # Add talker.py here
  scripts/relay.py        # Add relay.py here
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
