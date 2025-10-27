#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Enter a positive integer: ";
    cin >> N;
    long long fact = 1; // avoid overflow

    for (int i = 1; i <= N; i++) {
        fact *= i; 
    }

//    while (i <= N) {
//        fact *= i;
//        i++;
//    }

    cout << "Factorial (for loop): " << fact << endl;
    return 0;
}

