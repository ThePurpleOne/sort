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

def add_to_file(text, filename="logs.txt"):
	with open(filename, "a") as f:
		f.write(text)

def main():
	from sort import bubble, selection, insertion, merge, quick, python 

	n_items = 1000
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

	add_to_file(f"{'':-^50}\nitems:{n_items}\n")
	for name, func in sort_algos.items():
		a = numbers[::]
		print(f"{name:-^50}")
		time, sorted_array = test(func, a)
		print(f"{name:<20}: {time * 1000:.05f} ms")
		add_to_file(f"{name:<20}:{time * 1000:<8.05f}ms\n")
	print("\n")

if __name__ == "__main__":
	main()