#include <iostream>
using namespace std;

int main() {
    int N;
    cout << "Enter array size: ";
    cin >> N;

    int* arr = new int[N];
    cout << "Array elements: ";
    for (int i = 0; i < N; i++) {
        arr[i] = i * i;
        cout << arr[i] << " ";
    }
    cout << endl;

    delete[] arr;

    return 0;
}

