def quick_sort(array):
  return helper(array, 0, len(array) - 1)

def helper(array, first, last):
  if first < last:
    split = partition(array, first, last)
    helper(array, first, split - 1)
    helper(array, split + 1, last)
  return array

def partition(array, first, last):
  pivot = array[first]
  left = first + 1
  right = last
  done = False
  while not done:
     while left <= right and array[left] <= pivot:
        left = left + 1
     while array[right] >= pivot and right >= left:
        right = right -1
     if right < left:
        done = True
     else:
       temp = array[left]
       array[left] = array[right]
       array[right] = temp
  temp = array[first]
  array[first] = array[right]
  array[right] = temp
  return right

print quick_sort([5,1,3,8,5,3,4,67,45,2,8,5,34])
