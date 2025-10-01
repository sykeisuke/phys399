def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None

if __name__ == "__main__":
    nums = [2, 3, 5, 7, 9, 12, 13, 15, 16, 19, 21]
    target = 23
    print(f"nums:{nums}, target:{target}")
    print(two_sum(nums, target))

