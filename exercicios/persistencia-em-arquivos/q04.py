#Crie um programa que abra o arquivo "dados.txt" e conte o número de linhas que existem nele, exibindo o resultado na tela.

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  

# Exibindo o número de linhas
print(f"O arquivo contém {len(linhas)} linhas.")

