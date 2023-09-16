cmake_minimum_required(VERSION 3.8)
project(rbtspc_wp_flwr)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(joy REQUIRED)
find_package(teleop_twist_joy)
find_package(turtlebot3_gazebo)

install (PROGRAMS 
  scripts/publish_goal.py
  scripts/navigation_action_publisher.py
  DESTINATION lib/${PROJECT_NAME}
  )

install (DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
  )


ament_package()
