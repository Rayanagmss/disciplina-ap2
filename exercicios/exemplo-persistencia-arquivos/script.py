import os
import os.path

def imprime_menu():
    print(" Cadastro de Aluno:")
    print(" 1. Novo")
    print(" 2. Lista")
    print(" --------")
    print(" 9. Sair")

def novo_aluno(lista):
    print("------------------------")
    print("NOVO ALUNO:")
    matricula = input("Matricula:")
    nome = input("Nome:")
    curso = input("Curso:")
    aluno = []
    aluno.append(matricula)
    aluno.append(nome)
    aluno.append(curso)
    lista.append(aluno)

def imprime_alunos(alunos):
    print("------------------------")
    print("ALUNOS CADASTRADOS:")
    for aluno in alunos:
        print("Matricula:",aluno[0])
        print("Nome:",aluno[1])
        print("Curso:",aluno[2])
        print("--------------------")
    
def carrega_dados(NOME_ARQUIVO):
    lista_carregada = []
    if os.path.exists(NOME_ARQUIVO):
        arquivo = open(NOME_ARQUIVO, "r")
        for linha in arquivo.readlines():
            aluno = linha.split(";")
            lista_carregada.append(aluno)
        return lista_carregada
    else:
        return []

def salvar_arquivo(NOME_ARQUIVO, alunos):
    SEPARADOR = ";"
    arquivo = open(NOME_ARQUIVO, "w")
    for aluno in alunos:
        arquivo.write(aluno[0]+SEPARADOR+aluno[1]+SEPARADOR+aluno[2]+SEPARADOR+"\n")
    arquivo.close()

def limpa_tela():
    os.system("clear")

# Programa Principal:

NOME_ARQUIVO = "dados.dat"
lista = carrega_dados(NOME_ARQUIVO)
opcao = 1
limpa_tela()
while (opcao!=9):
    imprime_menu()
    opcao = int(input("Informe opcao desejada:"))
    if (opcao ==1):
        novo_aluno(lista)    
    elif (opcao == 2):
        imprime_alunos(lista)
    input("\nDigite [ENTER]")
    limpa_tela()
salvar_arquivo(NOME_ARQUIVO, lista)
#exemplo