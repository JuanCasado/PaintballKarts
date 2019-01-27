cmake_minimum_required(VERSION 3.10)
project(PaintballKarts)

set(CMAKE_CXX_STANDARD 11)

find_package(OpenCV REQUIRED)

include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable(PaintballKarts main.cpp Map.cpp Map.hpp Car.cpp Car.hpp Simulation.cpp Simulation.hpp)
target_link_libraries(PaintballKarts ${OpenCV_LIBS} )
