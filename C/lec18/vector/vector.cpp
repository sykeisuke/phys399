#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> data;      // empty vector
    data.push_back(10);    // add element
    data.push_back(20);

    cout << "Size: " << data.size() << endl;
    cout << "First: " << data[0] << endl;

    return 0;
}

