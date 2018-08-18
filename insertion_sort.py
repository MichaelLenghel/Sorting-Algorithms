# Insertion sort algorithm

def insertion_sort(li):
	for x in range(0, len(li) - 1):
		i = x
		while li[i + 1] < li[i] and i >= 0:
			li[i + 1], li[i] = li[i], li[i + 1]
			i -= 1
	return li

if __name__ == '__main__':
	li = [9, 5, 18, 10, 19, 4, 9, 16, 12, 20]

	print("Unsorted list:")
	for x in li:
		print(x, end=", ")

	print("\n")
	li_2 = insertion_sort(li)

	print("Sorted list: ")
	for x in li_2:
		print(x, end=", ")