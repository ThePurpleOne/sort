import numpy as np
import tqdm 

def bubble(numbers):
	for j in range(len(numbers)-1, -1, -1):
		swapped = False
		for i in range(j):
			if numbers[i+1] < numbers[i]:
				numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
				swapped = True
		if not swapped:
			break

def selection(numbers):
	s = len(numbers)
	for i in range(s):
		min_index = i
		for y in range(i + 1, s):
			if numbers[y] < numbers[min_index]:
				min_index = y
		# Get the min to the correct pos
		numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

def insertion(numbers):
	i = 1
	while i < len(numbers):
		x = numbers[i]
		j = i - 1
		while j >= 0 and numbers[j] > x:
			numbers[j+1] = numbers[j]
			j = j - 1
		numbers[j+1] = x
		i = i + 1

def merge(numbers):
	# STOLEN FROM https://www.educative.io/answers/merge-sort-in-python
	if len(numbers) > 1:
		mid = len(numbers) // 2
		left = numbers[:mid]
		right = numbers[mid:]

		# Recursive call on each half
		merge(left)
		merge(right)
		# Two iterators for traversing the two halves
		i = 0
		j = 0

		# Iterator for the main list
		k = 0

		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				# The value from the left half has been used
				numbers[k] = left[i]
				# Move the iterator forward
				i += 1
			else:
				numbers[k] = right[j]
				j += 1
			# Move to the next slot
			k += 1

		# For all the remaining values
		while i < len(left):
			numbers[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			numbers[k]=right[j]
			j += 1
			k += 1

def quick(numbers):
	quick_helper(numbers, 0, len(numbers) - 1)

def quick_helper(numbers, low, high):
	if low < high:
		pivot = partition(numbers, low, high)
		quick_helper(numbers, low, pivot - 1)
		quick_helper(numbers, pivot + 1, high)

def partition(numbers, low, high):
	i = low - 1
	pivot = numbers[high // 2]

	for j in range(low, high):
		if numbers[j] <= pivot:
			i += 1
			numbers[i], numbers[j] = numbers[j], numbers[i]

	numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
	return i + 1

def python(numbers):
	numbers.sort()

def test_algo(func, numbers, already_sorted):
	func(numbers)
	print(f"Should be sorted {numbers}")
	if numbers == already_sorted:
		print(f"{func.__name__:<28} ✅")
	else:
		print(f"{func.__name__:<28} ❌")

if __name__ == "__main__":
	# TESING IF EVERY ALGO WORKS CORRECTLY
	import random
	n = 10
	numbers = [random.randint(0, 1000) for i in range(n)]

	sort_algos = {
		"Bubble": bubble,
		"Selection": selection,
		"Insertion": insertion,
		"Merge": merge,
		"Quick": quick,
		"Python" : python
	}


	print(f"{'TESTING ALGORITHMS':-^30}")
	for name, func in sort_algos.items():
		a = numbers[:] # create copy
		test_algo(func, a, sorted(numbers))