def longest_common_prefix(strs):

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1] 
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    print(longest_common_prefix(strs1))  # "fl"
    strs2 = ["dog", "car", "racecar"]
    print(longest_common_prefix(strs2))  # ""

