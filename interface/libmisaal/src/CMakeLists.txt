set(LIBMISAAL_SRC
    misaal.cpp
)

# Form the full path to the source files...
PREPEND(LIBMISAAL_SRC)
# ... and pass the variable to the parent scope.
set(LIBMISAAL_SRC ${LIBMISAAL_SRC}  PARENT_SCOPE)
