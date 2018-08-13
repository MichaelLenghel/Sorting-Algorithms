""" 
radix sort: Time compelxity
where n is the number of elements, d the number of digits and b is base ten system. So b = 10
			We use counting court which is o(n + k) where k is the number of keys that we have for each number (which is b i.e. 10)
											so o(n + b) repeated for b times. i.e. the number of digits in the bigesst number
											so o(d(n + b)). Based on the  size of input relative to digits, can outperform quick or merge sort                                   
			Best case
			Medium case
			worst case
"""
def radix_sort(arr):
	# Getting the number of digits the biggest number in the list has
	m = len(str(max(arr)))

	# Make each number the same size as the biggest number, by adding zeros to the front.
	for i, n in enumerate(arr):
		# Find number of digits required to be same size as biggest number
		digit_gain = m - len(str(arr[i]))
		# Add zeros in front of the number to be the same size
		for j in range(0, digit_gain):
			arr[i] = str(0) + str(arr[i])
			arr[i] = arr[i]

	sorted_array_0 = list()
	sorted_array_1 = list()
	sorted_array_2 = list()
	sorted_array_3 = list()
	sorted_array_4 = list()
	sorted_array_5 = list()
	sorted_array_6 = list()
	sorted_array_7 = list()
	sorted_array_8 = list()
	sorted_array_9 = list()

	# Repeats for each digit. Where m is the no. of digits we have
	for j in range(0, m):
		# repeat for each element on the last digit
		for i, n in enumerate(arr):
			# m is 1 - 4. Minus one and we go 0 - 3
			if str(arr[i])[m - j - 1] == '0':
				sorted_array_0.append(n)
			elif str(arr[i])[m - j - 1] == '1':
				sorted_array_1.append(n)
			elif str(arr[i])[m - j - 1] == '2':
				sorted_array_2.append(n)
			elif str(arr[i])[m - j - 1] == '3':
				sorted_array_3.append(n)					
			elif str(arr[i])[m - j - 1] == '4':
				sorted_array_4.append(n)
			elif str(arr[i])[m - j -1] == '5':
				sorted_array_5.append(n)
			elif str(arr[i])[m - j - 1] == '6':
				sorted_array_6.append(n)
			elif str(arr[i])[m - j - 1] == '7':
				sorted_array_7.append(n)
			elif str(arr[i])[m - j - 1] == '8':
				sorted_array_8.append(n)
			elif str(arr[i])[m - j - 1] == '9':
				sorted_array_9.append(n)

		# Take out the numbers from array_0 ... array_9
		arr.clear()
		arr = sorted_array_0 + sorted_array_1 + sorted_array_2 + sorted_array_3 \
				+ sorted_array_4  + sorted_array_5 +  sorted_array_6  + sorted_array_7 \
				+ sorted_array_8  + sorted_array_9
		sorted_array_0.clear()
		sorted_array_1.clear()
		sorted_array_2.clear()
		sorted_array_3.clear()
		sorted_array_4.clear()
		sorted_array_5.clear()
		sorted_array_6.clear()
		sorted_array_7.clear()
		sorted_array_8.clear()
		sorted_array_9.clear()
	
	arr_formated = [int(x) for x in arr]
	return arr_formated


if __name__ == '__main__':
    arr = list(map(int, input("Enter integers, separated by spaces\n").rstrip().split()))

    print("Orignal array:", arr)

    arr = radix_sort(arr)

    print(arr)