# Calcule e mostre quantos anos serão necessários para que Ana seja maior que  Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 me cresce 2 cm ao ano.

def main():
    altura_ana = 1.10
    altura_maria = 1.50
    crescimento_ana = 0.03
    crescimento_maria = 0.02
    anos = 0

    while altura_ana <= altura_maria:
        altura_ana += crescimento_ana
        altura_maria += crescimento_maria
        anos += 1

    print(f"Serão necessários {anos} anos para que Ana seja maior que Maria.")
main()