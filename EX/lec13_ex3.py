def merge_sorted_lists(list1, list2):
    i, j = 0, 0  
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

if __name__ == "__main__":
    list1 = [1, 2, 3, 5, 6, 8, 9]
    list2 = [2, 3, 5, 7, 10]
    print(merge_sorted_lists(list1, list2))
