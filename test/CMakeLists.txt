# Set some variables
set(BINARY ${CMAKE_PROJECT_NAME}_test)
set(LIBS Formula_test)

add_library(Formula_test Formula.test.cpp)

# Create the tests as an executable
add_executable(${BINARY} main.cpp)

# Add Testing Libraries to Binary
target_link_libraries(${BINARY} PUBLIC ${LIBS}) 

# Create dependency of ${BINARY} on googletest
add_dependencies(${BINARY} googletest)

target_link_libraries(${BINARY} PUBLIC gtest gtest_main pthread)

# Name test cases
add_test(NAME ${BINARY} COMMAND ${BINARY})
