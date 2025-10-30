#include <iostream>
#include <cmath>
#include "particle.h"
using namespace std;

// Constructor
Particle::Particle(string n, double m, double px_, double py_, double pz_) {
    name = n;
    mass = m;
    px = px_;
    py = py_;
    pz = pz_;
}

// Methods
double Particle::momentum() {
    return sqrt(px*px + py*py + pz*pz);
}

double Particle::energy() {
    return sqrt(momentum()*momentum() + mass*mass);
}

void Particle::printInfo() {
    cout << "Particle: " << name << endl;
    cout << "Mass: " << mass << " GeV/c^2" << endl;
    cout << "Momentum: " << momentum() << " GeV/c" << endl;
    cout << "Energy: " << energy() << " GeV" << endl;
    cout << "-----------------------------" << endl;
}

