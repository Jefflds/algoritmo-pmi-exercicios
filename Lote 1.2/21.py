#Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
#a. Se a média for >= 6,0 exibir “APROVADO”;
#b. Se a média for >= 3,0 E < 6,0 exibir “EXAME”;
#c. Se a média for < 3,0 exibir “RETIDO”.

def main():
    try:
        n1_str = input("Informe a primeira nota: ").strip()
        n1 = float(n1_str.replace(',', '.'))
        n2_str = input("Informe a segunda nota: ").strip()
        n2 = float(n2_str.replace(',', '.'))
        n3_str = input("Informe a terceira nota: ").strip()
        n3 = float(n3_str.replace(',', '.'))
        n4_str = input("Informe a quarta nota: ").strip()
        n4 = float(n4_str.replace(',', '.'))
    except ValueError:
        print("Entrada inválida. Informe números válidos.")
        return

    media = (n1 + n2 + n3 + n4) / 4

    if media >= 6.0:
        print("APROVADO")
    elif media >= 3.0:
        print("EXAME")
    else:
        print("RETIDO")

main()