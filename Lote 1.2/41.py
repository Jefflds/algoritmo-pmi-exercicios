# Mostre todas as possibilidades de 2 dados de forma que a soma seja 7.

def pares_soma_7():
	resultados = []
	for d1 in range(1, 7):
		for d2 in range(1, 7):
			if d1 + d2 == 7:
				resultados.append((d1, d2))
	return resultados


def main():
	possiveis = pares_soma_7()
	for d1, d2 in possiveis:
		print(f"Dado1: {d1}, Dado2: {d2} -> Soma: {d1 + d2}")
	print(f"Total de possibilidades: {len(possiveis)}")

main()
