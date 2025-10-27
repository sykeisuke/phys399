int x = 10;
if (x > 0) {
    cout << "Positive" << endl;
}
else if (x == 0) {
    cout << "Zero" << endl;
}
else {
    cout << "Negative" << endl;
}

int day = 3;

switch (day) {
    case 1:
        cout << "Monday" << endl;
        break;
    case 2:
        cout << "Tuesday" << endl;
        break;
    case 3:
        cout << "Wednesday" << endl;
        break;
    default:
        cout << "Invalid day" << endl;
}


for (int i = 0; i < 5; i++) {
    cout << "i =" << i << endl;
}

int i = 0;
while (i < 5) {
    cout << i << " ";
    i++;
}

int j = 0;
do {
    cout << j << " ";
    j++;
} while (j < 5);

for (int i = 0; i < 5; i++) {
    cout << i << endl;
}

int add(int a, int b) {
    return a + b;
}


int add(int a, int b) {
    return a + b;
}

int main() {
    cout << add(2, 3);
    return 0;
}

int arr[5] = {1, 2, 3, 4, 5};

int x = 10; // normal variable
int* p = &x; // pointer to x
cout << "x =" << x << endl; // prints 10
cout << "&x = " << &x << endl; // prints address of x
cout << "p = " << p << endl; // same as &x
cout << "*p = " << p* << endl; // value pointed by p

