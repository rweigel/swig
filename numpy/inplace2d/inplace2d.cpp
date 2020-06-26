void inplace2d(double* npyArray2D, int npyLength1D, int npyLength2D)
{
    for(int i = 0; i < npyLength1D; ++i)
    {
        for(int j = 0; j < npyLength2D; ++j)
        {
            int nIndexJ = i * npyLength2D + j;
            // operate on array
            npyArray2D[nIndexJ] = 3.0;
        }
    }
}