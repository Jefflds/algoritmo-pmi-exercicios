# Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.

while True:
    userXInput = input("Digite o valor de x (ou 'S' para sair): ")
    if userXInput.upper() == 'S':
        break

    userYInput = input("Digite o valor de y: ")

    # Efetuar troca
    userXInput, userYInput = userYInput, userXInput
    print("Após a troca:")
    print("x:", userXInput)
    print("y:", userYInput)