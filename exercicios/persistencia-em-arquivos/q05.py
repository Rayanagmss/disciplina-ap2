#Escreva um programa que leia um arquivo de texto chamado "numeros.txt", onde cada linha contém um número inteiro. O programa deve calcular e exibir a soma de todos os números.
try:
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        soma = sum(int(linha.strip()) for linha in arquivo)  
    print(f"A soma dos números é: {soma}")
except FileNotFoundError:
    print("O arquivo 'numeros.txt' não foi encontrado.")
except ValueError:
    print("O arquivo contém valores inválidos. Certifique-se de que todas as linhas possuem números inteiros.")
