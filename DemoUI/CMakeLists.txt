cmake_minimum_required(VERSION 3.5)
project(DemoUI)

# Enable automatic MOC, UIC, and RCC processing
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

# Find necessary Qt5 components
find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets Svg Script)

# Include project directories
include_directories(
    ${Cornucopia_SOURCE_DIR}/Cornucopia
    ${Cornucopia_SOURCE_DIR}/DemoUI
    ${CMAKE_CURRENT_BINARY_DIR}  # For moc output
)

# Gather source files
file(GLOB DemoUI_CPP "*.cpp")
file(GLOB DemoUI_H "*.h")
file(GLOB DemoUI_UI "*.ui")

# Combine all sources
set(DemoUI_Sources ${DemoUI_CPP} ${DemoUI_H} ${DemoUI_UI})

# Add executable target
add_executable(DemoUI ${DemoUI_Sources})

# Link required libraries
target_link_libraries(DemoUI
    Cornucopia
    Qt5::Core
    Qt5::Gui
    Qt5::Widgets
    Qt5::Svg
    Qt5::Script
)

# Install binary
install(TARGETS DemoUI RUNTIME DESTINATION bin)

# Windows-specific Qt DLL installation
if(WIN32)
    install(FILES
        "${QT_BINARY_DIR}/Qt5Core.dll"
        "${QT_BINARY_DIR}/Qt5Gui.dll"
        "${QT_BINARY_DIR}/Qt5Script.dll"
        DESTINATION bin
    )
endif()
