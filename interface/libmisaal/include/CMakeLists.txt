set(LIBMISAAL_INC
    misaal.h
)

# Form the full path to the source files...
PREPEND(LIBMISAAL_INC)
# ... and pass the variable to the parent scope.
set(LIBMISAAL_INC ${LIBMISAAL_INC}  PARENT_SCOPE)
