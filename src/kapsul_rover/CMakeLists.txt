cmake_minimum_required(VERSION 2.8.3)

project(kapsul_rover)

catkin_package()

find_package(catkin REQUIRED COMPONENTS
roscpp 
std_msgs 
actionlib
move_base_msgs
sensor_msgs 
roslaunch
)

include_directories(${catkin_INCLUDE_DIRS})

add_executable(simple_navigation_goals src/simple_navigation_goals.cpp)
target_link_libraries(simple_navigation_goals ${catkin_LIBRARIES})	

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
