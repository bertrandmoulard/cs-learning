def merge_sort(a):
  if len(a) > 1:
    left = merge_sort(a[0:len(a)/2])
    right = merge_sort(a[len(a)/2:])
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        a[k] = left[i]
        i += 1
      else:
        a[k] = right[j]
        j += 1
      k += 1
    while i < len(left):
      a[k] = left[i]
      k += 1
      i += 1
    while j < len(right):
      a[k] = right[j]
      k += 1
      j += 1
  return a

assert(merge_sort([]) == [])
assert(merge_sort([1]) == [1])
assert(merge_sort([1, 2]) == [1, 2])
assert(merge_sort([2, 1]) == [1, 2])
assert(merge_sort([4, 4, 1, 3, 2, 5, 4, 4]) == [1, 2, 3, 4, 4, 4, 4, 5])
assert(merge_sort([5, 9, 7, 2, 4, 3, 1]) == [1, 2, 3, 4, 5, 7, 9])
