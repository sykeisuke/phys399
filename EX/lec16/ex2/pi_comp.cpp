#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double PI = 3.14159265358979;
    int pi_i = PI;
    float pi_f = PI;
    double pi_d = PI;

    cout << fixed << setprecision(15);
    cout << "int:    " << pi_i << endl;
    cout << "float:  " << pi_f << endl;
    cout << "double: " << pi_d << endl;
    return 0;
}

