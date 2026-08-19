#Bibliotecas usadas e import do SO
from cryptography.fernet import Fernet
import os

#Função que vai retornas o conteúdo ao normal
def carregar_chave():
    return open("chave.key", "rb").read()

def decriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

#Localizador do arquivo no SO
def encontrararquivos(diretorio):
    lista = []
    for raiz,  arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#Função que carrega as chaves e retorna o arquivo ao seu estado normal
def main():
    chave = carregar_chave()
    arquivos= encontrararquivos("test_files")
    for arquivo in arquivos:
        decriptografar_arquivo(arquivo, chave)
    print("Arquivos restaurados com sucesso")


if __name__ == "__main__":
    main()
