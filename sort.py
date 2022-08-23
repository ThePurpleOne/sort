import numpy as np
import tqdm 





def test(func, numbers, rep=10):
	import time

	avg = 0
	for i in tqdm.tqdm(range(rep), bar_format='{l_bar}{bar:20}{r_bar}'):
		start = time.perf_counter()
		sorted_arr = func(numbers)
		end = time.perf_counter()
		avg += end - start

	return (avg / rep), sorted_arr

def bubble(numbers):
	for i in range(len(numbers)):
		for j in range(len(numbers) - 1):
			if numbers[j] > numbers[j + 1]:
				numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
	return numbers

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
	return numbers

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


def main():
	import random

	n = 100
	#numbers = np.array([random.randint(0, 1000) for i in range(n)], dtype=np.int32)
	numbers = [random.randint(0, 1000) for i in range(n)]
	
	sort_algos = {
		"Bubble": bubble,
		"Selection": selection,
		"Insertion": insertion,
		"Merge": merge,
	}

	for name, func in sort_algos.items():
		a = numbers[:]
		print(f"{name:-^50}")
		time, sorted_array = test(func, a)
		print(f"{name:<20}: {time * 1000} ms")


if __name__ == "__main__":
	main()