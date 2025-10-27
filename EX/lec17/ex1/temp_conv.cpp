#include <iostream>
using namespace std;

int main() {
    double celsius;
    cout << "Enter temperature in Celsius: ";
    cin >> celsius;

    double fahrenheit = (9.0 / 5.0) * celsius + 32;
    cout << "Temperature in Fahrenheit: " << fahrenheit << endl;
    return 0;
}
