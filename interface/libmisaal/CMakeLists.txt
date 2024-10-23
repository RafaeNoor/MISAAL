cmake_minimum_required(VERSION 3.1)
set(CMAKE_CXX_STANDARD 11)


project(LIBMISAAL VERSION 1.0)
set(LIBMISAAL_VERSION 1.0)



# Function to prepend the subdirectory to source files in subdirectories
function(PREPEND var )
   set(listVar "")
   foreach(f ${${var}})
       list(APPEND listVar "${CMAKE_CURRENT_SOURCE_DIR}/${f}")
   endforeach(f)
   set(${var} "${listVar}" PARENT_SCOPE)
endfunction(PREPEND)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/bin")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lib")

#include_directories(include)

add_subdirectory(src)
add_subdirectory(include)


add_library(LIBMISAAL STATIC ${LIBMISAAL_SRC} ${LIBMISAAL_INC})

target_include_directories(LIBMISAAL PUBLIC
   # headers to include when building from source
   $<BUILD_INTERFACE:${LIBMISAAL_SOURCE_DIR}/include>
   $<BUILD_INTERFACE:${LIBMISAAL_BINARY_DIR}/include>

   # headers to include when installing
   # (implicitly prefixes with ${CMAKE_INSTALL_PREFIX}).
   $<INSTALL_INTERFACE:include>
   )

include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    LIBMISAALConfigVersion.cmake
    VERSION ${LIBMISAAL_VERSION}
    COMPATIBILITY AnyNewerVersion
    )

