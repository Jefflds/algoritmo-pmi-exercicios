# Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

def series_sum(n=50):
	total = 0.0
	for i in range(1, n + 1):
		denom = 2 * i - 1
		total += i / denom
	return total


if __name__ == "__main__":
	resultado = series_sum(50)
	print(f"Soma da série 1 + 2/3 + ... + 50/99 = {resultado:.6f}")