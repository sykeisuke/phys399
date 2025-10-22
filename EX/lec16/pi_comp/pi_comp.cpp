#include <iostream>
#include <iomanip>
#include <cmath>   // for M_PI

using namespace std;

int main() {
    int pi_i = M_PI;           
    float pi_f = M_PI;         
    double pi_d = M_PI;        

    cout << fixed << setprecision(15);
    cout << "M_PI (true)   = " << M_PI  << endl;
    cout << "int    pi_i   = " << pi_i  << endl;
    cout << "float  pi_f   = " << pi_f  << endl;
    cout << "double pi_d   = " << pi_d  << endl;

    return 0;
}

