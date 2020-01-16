cmake_minimum_required(VERSION 3.10)

project(GTProject VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

include_directories(/usr/local/include)

# Enable the "make test" command
ENABLE_TESTING()

add_subdirectory(src EXE)
add_subdirectory(test TESTS)
