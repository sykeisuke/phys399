#include <iostream>
using namespace std;

class Car {
private:
    string model;       // car model name
    float fuel;         // remaining fuel [L]
    float efficiency;   // fuel efficiency [km/L]

public:
    Car(float f, float e) {   // constructor
        fuel = f;
        efficiency = e;
    }

    void drive(float distance) {
        float required = distance / efficiency;
        if (required <= fuel) {
            fuel -= required;
            cout << "Drove " << distance << " km." << endl;
        } else {
            cout << "Not enough fuel!" << endl;
        }
    }

    void refuel(float L) {
        fuel += L;
        cout << "Refueled " << L << " L." << endl;
    }

    float getFuel() {
        return fuel;
    }
};

int main() {
    Car c1(10.0, 15.0);  // 10 L fuel, 15 km/L efficiency
    c1.drive(100);       // ✅ uses public method
    c1.refuel(5);
    cout << "Remaining fuel: " << c1.getFuel() << " L" << endl;
    return 0;
}

