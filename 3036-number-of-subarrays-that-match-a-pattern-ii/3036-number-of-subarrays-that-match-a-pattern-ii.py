def countPattern(nums, pattern):
    n = len(nums)
    m = len(pattern)
    
    # Step 1: Convert pattern to the comparison relations.
    rel_pattern = []
    for i in range(m):
        if pattern[i] == 1:
            rel_pattern.append(1)
        elif pattern[i] == 0:
            rel_pattern.append(0)
        elif pattern[i] == -1:
            rel_pattern.append(-1)
    
    # Step 2: Create the relations array for nums
    relations = []
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            relations.append(1)
        elif nums[i] == nums[i - 1]:
            relations.append(0)
        else:
            relations.append(-1)

    # Step 3: Apply KMP algorithm to find pattern in relations array
    # Compute the lps (longest prefix suffix) array for the pattern
    lps = [0] * m
    j = 0  # Length of the previous longest prefix suffix
    for i in range(1, m):
        while (j > 0 and rel_pattern[i] != rel_pattern[j]):
            j = lps[j - 1]
        if rel_pattern[i] == rel_pattern[j]:
            j += 1
            lps[i] = j

    # Step 4: KMP search
    result = 0
    j = 0  # Index for pattern
    for i in range(n - 1):  # Traverse the relations array
        while (j > 0 and relations[i] != rel_pattern[j]):
            j = lps[j - 1]
        if relations[i] == rel_pattern[j]:
            j += 1
        if j == m:  # Found a match
            result += 1
            j = lps[j - 1]
    
    return result