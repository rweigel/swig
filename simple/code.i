%module code
%{
#include "code.h"
%}

%include "std_vector.i"

%template(FloatVector) std::vector<float>;

%include "code.h"
