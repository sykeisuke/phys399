#include <iostream>
using namespace std;

int main () {
    int x = 10; 
    int* p = &x; 

    cout << "x =" << x << endl; 
    cout << "&x = " << &x << endl; 
    cout << "p = " << p << endl; 
    cout << "*p = " << *p << endl; 

    *p = 20;
    cout << "x (after *p = 20) = " << x << endl;

    return 0;
}

