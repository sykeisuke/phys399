#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Enter a positive integer N: ";
    cin >> N;
    cout << "Even numbers between 1 and " << N << ":" << endl;

    for (int i = 1; i <= N; i++) {
        if (i % 2 == 0) {
            cout << i << " ";
        }
    }
    cout << endl;
    return 0;
}

