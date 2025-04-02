#Escreva um programa em Python que adicione a frase "Bem-vindo ao curso de Introdução à Programação!" no final do arquivo "dados.txt" sem sobrescrever o conteúdo existente.
with open("dados.txt", "a") as file:
    file.write("\nBem-vindo ao curso de Introdução à Programação!")