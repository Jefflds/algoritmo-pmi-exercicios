# Receba 2 números inteiros e mostre todos os números primos entre eles.


from __future__ import annotations
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_between(a: int, b: int) -> list[int]:
    start, end = sorted((a, b))
    return [n for n in range(start, end + 1) if is_prime(n)]


def main() -> None:
    try:
        a = int(input("Digite o primeiro número inteiro: "))
        b = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Por favor, insira números inteiros válidos.")
        return

    primes = primes_between(a, b)
    lo, hi = min(a, b), max(a, b)
    if primes:
        print(f"Números primos entre {lo} e {hi}:")
        for p in primes:
            print(p)
    else:
        print(f"Não há números primos entre {lo} e {hi}.")

main()