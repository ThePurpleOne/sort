import random
import time
import tqdm


def test(func, numbers, rep=1000):

	avg = 0
	for i in tqdm.tqdm(range(rep), bar_format='{l_bar}{bar:20}{r_bar}'):
		start = time.perf_counter()
		sorted_arr = func(numbers)
		end = time.perf_counter()
		avg += end - start

	return (avg / rep), sorted_arr

def main():
	from sort import bubble, selection, insertion, merge, quick, python 

	n_items = 10
	numbers = [random.randint(0, 10000) for i in range(n_items)]
	
	sort_algos = {
		"Bubble": bubble,
		"Selection": selection,
		"Insertion": insertion,
		"Merge": merge,
		"Quick": quick,
		"Python" : python
	}


	print(f"\n\n\n{'':-^50}")
	print(f"{f'  TESTING WITH {n_items} ITEMS LISTS  ':-^50}")
	print(f"{'':-^50}\n")
	for name, func in sort_algos.items():
		a = numbers[:]
		print(f"{name:-^50}")
		time, sorted_array = test(func, a)
		print(f"{name:<20}: {time * 1000} ms")
	print("\n")



if __name__ == "__main__":
	main()