import sys

arr = []
print(f"len={len(arr)}, bytes={sys.getsizeof(arr)}")

for i in range(50):
    arr.append(i)
    if i % 5 == 0:
        print(f"len={len(arr)}, bytes={sys.getsizeof(arr)}")


arr = []
for i in range(50):
    arr.append(i)


