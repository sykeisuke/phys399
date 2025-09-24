def lifetime_stats(times: list) -> dict:
    result = {}
    total_count = 0
    for i in times:
        total_count += i
    result["average"] = total_count/len(times)
    #result["average"] = sum(times)/len(times)
    result["max"] = max(times)

    return result

decay_times = [2.1, 2.3, 1.9, 2.4, 2.0, 2.2]

print(lifetime_stats(decay_times))
