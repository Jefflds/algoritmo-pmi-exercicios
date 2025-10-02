# Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

altura_ana = 1.10  # metros
altura_maria = 1.50  # metros
crescimento_ana = 0.03  # 3 cm = 0.03 metros por ano
crescimento_maria = 0.02  # 2 cm = 0.02 metros por ano

if crescimento_ana <= crescimento_maria:
    print("Ana nunca será maior que Maria, pois cresce na mesma velocidade ou mais devagar.")
else:
    anos = 0
    print("Ano\tAltura Ana (m)\tAltura Maria (m)")
    print(f"{anos}\t{altura_ana:.2f}\t\t{altura_maria:.2f}")

    while altura_ana <= altura_maria:
        anos += 1
        altura_ana += crescimento_ana
        altura_maria += crescimento_maria
        print(f"{anos}\t{altura_ana:.2f}\t\t{altura_maria:.2f}")

    print(f"\nAna será maior que Maria após {anos} anos.")
    print(f"Ana terá {altura_ana:.2f}m e Maria terá {altura_maria:.2f}m")

input("Pressione Enter para sair...")