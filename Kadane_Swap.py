# MSS With Swaps - Maximum Subarray Sum after k swaps
# Idea: We can rearrange array partially using k swaps
# Goal: maximize contribution of largest values in a contiguous subarray

def max_subarray_sum(arr):
    """
    Standard Kadane's Algorithm to find Maximum Subarray Sum
    """
    cur = arr[0]
    mx = arr[0]

    for i in range(1, len(arr)):
        # Either extend previous subarray or start new one
        cur = max(arr[i], cur + arr[i])

        # Update global maximum
        mx = max(mx, cur)

    return mx


def solve(n, k, arr):
    """
    We try to maximize MSS after at most k swaps.
    Observation:
    - Each swap can help reposition elements
    - Best effect comes from bringing large values together
    """

    # Edge case: no swaps allowed
    if k == 0:
        return max_subarray_sum(arr)

    # Sort array to know largest elements
    sorted_arr = sorted(arr, reverse=True)

    # We can effectively "help" the top (k+1) elements become more contiguous
    # This is a heuristic based on swap flexibility
    top_elements = sorted_arr[:k + 1]

    # Combine original array with influence of top elements
    # Replace worst elements with best ones conceptually
    modified = arr[:]

    # Try to inject top values into array (greedy replacement idea)
    for i in range(min(len(modified), len(top_elements))):
        if modified[i] < top_elements[i]:
            modified[i] = top_elements[i]

    # Compute maximum subarray sum after modifications
    return max_subarray_sum(modified)


# ---------------- DRIVER CODE ----------------

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = [int(input().strip()) for _ in range(n)]

    result = solve(n, k, arr)
    print(result)
