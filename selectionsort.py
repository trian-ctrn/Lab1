def SelectionSort(arr):
	for i in range(len(arr)):
		low_index = i
		for j in range(i+1, len(arr)):
			if arr[low_index] > arr[j]:
				low_index = j
		arr[i], arr[low_index] = arr[low_index], arr[i]
	return arr
