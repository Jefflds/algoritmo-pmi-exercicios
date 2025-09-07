# Receba o raio de uma circunferência. Calcule e mostre o comprimento da circunferência.
# C = 2 * π * r (C = comprimento, r = raio, π = 3.14)

def main():
	try:
		raio_str = input("Informe o raio da circunferência: ").strip()
		raio = float(raio_str)
	except Exception:
		print("Entrada inválida. Informe um número para o raio.")
		return

	pi = 3.14
	comprimento = 2 * pi * raio
	print(f"Comprimento da circunferência: {comprimento:.2f}")


main()
