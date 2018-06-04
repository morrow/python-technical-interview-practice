def bubble_sort(array):
  # define maximum index to look at
  max = len(array) - 1
  # count down from maximum with each loop since we can assume the highest element bubbled up
  while max > 0:
    i = 0
    # track how many switches we make so we can return early if array is sorted
    switches = 0
    # go through array
    while i < max:
      # compare two side-by-side elements
      if array[i] > array[i + 1]:
        # if out of order, switch them
        higher = array[i]
        array[i] = array[i + 1]
        array[i + 1] = higher
        # track switches
        switches += 1
      i += 1
    if switches == 0:
      return array
    max -= 1
  return array

print bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14])