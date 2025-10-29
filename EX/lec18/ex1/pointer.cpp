#include <iostream>
using namespace std;

int main () {
    int a = 5;
    int b = 8; 
    int* p = &a; 

    cout << "a =" << a << endl; 
    cout << "b =" << b << endl; 
    cout << "*p = " << *p << endl; 
    cout << "&a = " << &a << endl; 
    cout << "&b = " << &b << endl; 
    cout << "p = " << p << endl; 

    p = &b;
    cout << "*p (p=&b) = " << *p << endl; 
    cout << "b (p=&b)=" << b << endl; 

    *p = 20;
    cout << "b (*p=20) =" << b << endl; 

    return 0;
}

