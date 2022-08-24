import random
import time
import tqdm


def test(func, numbers, rep=100):

	avg = 0
	for i in tqdm.tqdm(range(rep), bar_format='{l_bar}{bar:20}{r_bar}'):
		start = time.perf_counter()
		sorted_arr = func(numbers)
		end = time.perf_counter()
		avg += end - start

	return (avg / rep), sorted_arr

def main():
	from sort import bubble, selection, insertion, merge, quick, python 

	n = 1000
	numbers = [random.randint(0, 1000) for i in range(n)]
	
	sort_algos = {
		"Bubble": bubble,
		"Selection": selection,
		"Insertion": insertion,
		"Merge": merge,
		"Quick": quick,
		"Python" : python
	}

	for name, func in sort_algos.items():
		a = numbers[:]
		print(f"{name:-^50}")
		time, sorted_array = test(func, a)
		print(f"{name:<20}: {time * 1000} ms")



if __name__ == "__main__":
	main()