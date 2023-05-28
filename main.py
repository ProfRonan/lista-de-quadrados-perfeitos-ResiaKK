numero = int(input("Digite um número inteiro: "))
numero_final = numero**numero

for i in range(1, int(numero) + 1):
        quadrado = i * i
        if quadrado <= numero_final:
            print(quadrado)




