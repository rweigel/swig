%module inplace2d

%{
    #define SWIG_FILE_WITH_INIT
    #include "inplace2d.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* INPLACE_ARRAY2, int DIM1, int DIM2) \
      {(double* npyArray2D, int npyLength1D, int npyLength2D)}
%include "inplace2d.h"
%clear (double* npyArray2D, int npyLength1D, int npyLength2D);