#Escreva um programa em Python que crie um arquivo de texto chamado "dados.txt" e escreva a frase "Olá, mundo!" dentro deste arquivo

with open("dados.txt", "w") as file:
    file.write("Ola, mundo!")
    file.close()