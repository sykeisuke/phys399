#include <iostream>
using namespace std;

class Car {
public:
    string model;       // car model name
    float fuel;         // remaining fuel [L]
    float efficiency;   // fuel efficiency [km/L]

    float calcRange() {
        return fuel * efficiency;
    }

    void printInfo() {
        cout << "Model: " << model << endl;
        cout << "Fuel: " << fuel << " L" << endl;
        cout << "Efficiency: " << efficiency << " km/L" << endl;
        cout << "Estimated Range: " << calcRange() << " km" << endl;
    }
};

int main() {
    Car c1 = {"Toyota", 10.0, 15.0};
    c1.printInfo();

    return 0;
}

