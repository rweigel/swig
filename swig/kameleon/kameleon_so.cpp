#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <ccmc/Kameleon.h>
#include <ccmc/FileReader.h>

std::vector<float> runner (char* filename1input, std::vector<float> x, std::vector<float> y, std::vector<float> z, int N) {

  ccmc::Kameleon kameleon1;

  //std::string filename1input;
  //filename1input = "3d__var_3_e20031120-070000-000.out.cdf";
  
  clock_t start = clock();

  long status1 = kameleon1.open(filename1input);

  if (status1 != ccmc::FileReader::OK) {
    //std::cout << "Could not open " << filename1input << " Exiting with code 1." << std::endl;
    return x;
  }
  std::cout << filename1input << ": Opened." << std::endl;

  std::cout << filename1input << ": Loading variable started." << std::endl;
  if (kameleon1.doesVariableExist("p")){
    kameleon1.loadVariable("p");
  } else {
    std::cout << "Variable does not exist. Exiting with code 1.";
    return x;
  }
  std::cout << filename1input << ": Loading variable finished." << std::endl;

  ccmc::Interpolator * interpolator1 = kameleon1.createNewInterpolator();

  std::cout << filename1input << ": Interpolation started." << std::endl;

  for (int k = 0; k < N; k++)
    {
      //value1(k,0) = interpolator1->interpolate("p",  v[k], 1.0, 1.0);
      x[k] = interpolator1->interpolate("p",  x[k], y[k], z[k]);
    }
  std::cout << filename1input << ": Interpolation finished." << std::endl;
  
  double duration = ( std::clock() - start ) / (double) CLOCKS_PER_SEC;
  std::cout << "Interpolation took " << (duration) << " s" << std::endl;

  //value1.clear();
  delete interpolator1;
  kameleon1.close();

  return x;
  
}
