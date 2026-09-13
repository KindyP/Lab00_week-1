def summarize_ranges(values):
    # Return "none" if the list is empty
    if len(values) == 0:
        return "none"
    ranges = []
    i = 0
    while i < len(values):
        start = values[i]
        # Keep moving forward as long as numbers are consecutive
        while i + 1 < len(values) and values[i + 1] == values[i] + 1:
            i += 1
        end = values[i]
        # Format as single numbere
        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "-" + str(end))
        i += 1
    # Join items with comma and space
    return ", ".join(ranges)
print(summarize_ranges([]))  # Expected: "none"
print(summarize_ranges([7]))  # Expected: "7"
print(summarize_ranges([1, 2, 3, 4, 5]))  # Expected: "1-5"
print(summarize_ranges([1, 3, 5, 7]))  # Expected: "1, 3, 5, 7"
print(summarize_ranges([1, 2, 3, 5, 7, 8, 9]))  # Expected: "1-3, 5, 7-9"
print(summarize_ranges([0, 1, 2, 6, 7, 10]))  # Expected: "0-2, 6-7, 10"
print(summarize_ranges([98, 99, 100]))  # Expected: "98-100"
print(summarize_ranges([2, 4, 5, 6, 9, 11, 12]))  # Expected: "2, 4-6, 9, 11-12"
