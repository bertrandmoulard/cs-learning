def quick_sort(a):
  quick_sort_section(a, 0, len(a) - 1)
  return a

def quick_sort_section(a, first, last):
  if last - first >= 0:
    pivot = first
    left = pivot + 1
    right = last
    while left < right:
      while a[right] >= a[pivot] and right > pivot:
        right -= 1
      while a[left] < a[pivot] and left < last:
        left += 1
      if left < right:
        a[left], a[right] = a[right], a[left]
    if a[pivot] > a[right]:
      a[pivot], a[right] = a[right], a[pivot]
    quick_sort_section(a, first, right - 1)
    quick_sort_section(a, right + 1, last)

assert(quick_sort([]) == [])
assert(quick_sort([1]) == [1])
assert(quick_sort([1, 2]) == [1, 2])
assert(quick_sort([2, 1]) == [1, 2])
assert(quick_sort([4, 4, 1, 3, 2, 5, 4, 4]) == [1, 2, 3, 4, 4, 4, 4, 5])
assert(quick_sort([5, 9, 7, 2, 4, 3, 1]) == [1, 2, 3, 4, 5, 7, 9])
