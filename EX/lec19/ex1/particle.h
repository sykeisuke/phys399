#ifndef PARTICLE_H
#define PARTICLE_H

#include <string>
using namespace std;

class Particle {
private:
    string name;
    double mass, px, py, pz;

public:
    // Constructor
    Particle(string n, double m, double px_, double py_, double pz_);

    // Methods
    double momentum();
    double energy();
    void printInfo();
};

#endif
