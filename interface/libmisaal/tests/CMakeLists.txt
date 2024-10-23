cmake_minimum_required(VERSION 3.1)
set(CMAKE_CXX_STANDARD 11)

# Explicitly list the test source code and headers. The Catch header-only unit
# test framework is stored in with the test source.
set(LIBMISAAL_TEST_SRC
    simple_driver.cpp
)
set(LIBMISAAL_TEST_HEADER

)

PREPEND(LIBMISAAL_TEST_SRC)

add_executable(SIMPLE_DRIVER_TEST ${LIBMISAAL_TEST_SRC} ${LIBMISAAL_TEST_HEADER})


# Enable testing via CTest
enable_testing()
# Add our test as runnable via CTest
add_test(NAME SIMPLE_DRIVER_TEST  COMMAND SIMPLE_DRIVER_TEST)

# Link our unit tests against the library we compiled
target_link_libraries(SIMPLE_DRIVER_TEST LIBMISAAL)

