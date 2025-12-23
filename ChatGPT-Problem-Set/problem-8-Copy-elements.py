def copy_elements(arr):
  new_arr = []

  if len(arr) == 0: return

  for i in arr:
    new_arr.append(i)
  return f"This is the new array: {new_arr}"
