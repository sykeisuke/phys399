#include <iostream>
#include <cmath>
using namespace std;

class Particle {
private:
    string name;
    double mass, px, py, pz;

public:
    // Constructor
    Particle(string n, double m, double px_, double py_, double pz_) {
        name = n;
        mass = m;
        px = px_; py = py_; pz = pz_;
    }

    double momentum() {
        return sqrt(px*px + py*py + pz*pz);
    }

    double energy() {
        return sqrt(momentum()*momentum() + mass*mass);
    }

    void printInfo() {
        cout << "Particle: " << name << endl;
        cout << "Mass: " << mass << " GeV/c^2" << endl;
        cout << "Momentum: " << momentum() << " GeV/c" << endl;
        cout << "Energy: " << energy() << " GeV" << endl;
    }
};

int main() {
    Particle e("electron", 0.000511, 0.1, 0.2, 0.3);
    e.printInfo();
    return 0;
}
