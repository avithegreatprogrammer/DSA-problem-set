def find_max_element(arr):
  max_j = arr[0]
  for i in range(len(arr)):
    if arr[i] > max_j:
      max_j = arr[i]
  return arr[i]
