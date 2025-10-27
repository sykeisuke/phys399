#include <iostream>
using namespace std;

int main () {
    int x = 10; // normal variable
    int *p = &x; // pointer to x
    cout << "x =" << x << endl; // prints 10
    cout << "&x = " << &x << endl; // prints address of x
    cout << "p = " << p << endl; // same as &x
    cout << "*p = " << *p << endl; // value pointed by p

    return 0;
}

