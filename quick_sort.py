def partition(a, start, end):
  pivot = a[start]
  left = start + 1
  right = end
  met = False

  # Iterate until i reaches j in the middle
  while not met:

    while left <= right and a[left] <= pivot:
    	left = left + 1

    while right >= left and a[right] >= pivot:
    	right = right - 1
      
    if left >= right:
    	met = True
    else:
    	a[left], a[right] = a[right], a[left]

  # Swap pivot with the position of j
  a[start], a[right] = a[right], a[start]

  return right

def quick_sort(li, l, r):
  if l < r:
    split = partition(li, l, r)
    quick_sort(li, l, split - 1)
    quick_sort(li, split + 1, r)

if __name__ == '__main__':
  li = [65, 72, 23, 36, 99, 20, 1, 44]
  # [8, 2, 5, 13, 4, 19, 12, 6, 3, 11, 10, 7, 9]

  print("Unsorted list: ", li)
  quick_sort(li, 0, len(li) - 1)
  print("Sorted list: ", li)
  