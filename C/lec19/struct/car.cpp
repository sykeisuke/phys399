#include <iostream>
using namespace std;

struct Car {
    string model;       // car model name
    float fuel;         // remaining fuel [L]
    float efficiency;   // fuel efficiency [km/L]
};

int main() {
    Car c1 = {"Toyota", 10.0, 15.0};
    float distance = c1.fuel * c1.efficiency;

    cout << "Model: " << c1.model << endl;
    cout << "Fuel: " << c1.fuel << " L" << endl;
    cout << "Efficiency: " << c1.efficiency << " km/L" << endl;
    cout << "Estimated Range: " << distance << " km" << endl;

    return 0;
}

