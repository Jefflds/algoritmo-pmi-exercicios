# Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225
def series_sum(n=15):
    total = 0.0
    for i in range(1, n + 1):
        denom = i * i
        if i % 2 == 0:
            total -= i / denom
        else:
            total += i / denom
    return total

def main():
    resultado = series_sum(15)
    print(f"Soma da série 1 - 2/4 + ... + 15/225 = {resultado:.6f}")

main()