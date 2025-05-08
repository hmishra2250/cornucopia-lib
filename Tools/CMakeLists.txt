cmake_minimum_required(VERSION 3.5)
project(CornucopiaTools)

# Enable Qt5 automatic handling of MOC, UIC, and RCC
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Find required Qt5 components
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets Svg)

# Gather source files
file(GLOB Tools_CPP "*.cpp")
file(GLOB Tools_H "*.h")
file(GLOB Tools_UI "*.ui")

# Combine source files
set(Tools_Sources ${Tools_CPP} ${Tools_H} ${Tools_UI})

# Include directories
include_directories(
    ${CMAKE_CURRENT_BINARY_DIR}      # for MOC
    ${CMAKE_BINARY_DIR}              # for config.h
    ${Cornucopia_SOURCE_DIR}/Cornucopia
)

# Add executable target
add_executable(CornucopiaTools ${Tools_Sources})

# Link Qt5 libraries and your own
target_link_libraries(CornucopiaTools
    Cornucopia
    Qt5::Core
    Qt5::Gui
    Qt5::Widgets
    Qt5::Svg
)

# Generate config.h from config.h.cmake
configure_file(config.h.cmake config.h)
