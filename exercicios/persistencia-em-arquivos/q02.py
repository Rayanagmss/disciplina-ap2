#Crie um programa que leia o conteúdo do arquivo "dados.txt" criado na questão anterior e exiba o conteúdo na tela.
with open("dados.txt", "r") as file:
    content = file.read()
    print(content)