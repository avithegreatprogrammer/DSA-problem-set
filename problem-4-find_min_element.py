def find_min_element(arr):
    min_j = arr[0]
    for i in range(len(arr)):
        if arr[i] < min_j:
            min_j = arr[i]
    return min_j
