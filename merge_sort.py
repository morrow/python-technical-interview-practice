def merge_sort(input_array):

  # check for base case
  if len(input_array) < 2:
    return input_array

  # initialize result and mid variables
  result = []
  mid = int(len(input_array)/2)

  # sort left and right sides of array recursively
  left = merge_sort(input_array[:mid])
  right = merge_sort(input_array[mid:])

  # merge sorted left and right sub-arrays
  while (len(left) > 0) and (len(right) > 0):
    if left[0] > right[0]:
      result.append(right.pop(0))
    else:
      result.append(left.pop(0))

  # return merged result
  result.extend(left+right)
  return result

print merge_sort([21, 4, 1, 3, 9, 20, 25])