# -*- coding: utf-8 -*-
import csv, sys

class LimpadorDeDados:
    
    #Inicializa o objeto, abrindo o arquivo
    def __init__(self):
        #Modificar o diretório onde se encontra o arquivo ".csv" antes de executar
        self.arquivo = open("C:/Users/RafinhaLundgren/Music/Documents/GitHub/arvoresdaserra/referencias/Arvores de Serra .csv", "r+b")
        self.linhas = []    
    
    #Separa o conteúdo do arquivo em uma lista bidimensional, utilizando o formato linhas[linha][cédula]
    def lerArquivo(self):
        for linha in self.arquivo:
            self.linhas.append(linha.split(";"))
    
    #Grava o conteúdo no arquivo original  
    def gravarArquivo(self):
        gravador = csv.writer(self.arquivo, delimiter=";", lineterminator = '')
        self.arquivo.seek(0)
        gravador.writerows(self.linhas)
        self.arquivo.close()
    
    #Chama o método para ler o arquivo
    #Procura por impurezas no conteúdo do arquivo e as modifica no padrão determinado.        
    #Chama o método para gravar o arquivo modificado
    def LimparDados(self):
        self.lerArquivo()
        for contador in range(1,len(self.linhas)):
            if (self.linhas[contador][4] != "s/n") and (not(self.linhas[contador][4].isdigit())) or self.linhas[contador][4] == "0":
                self.linhas[contador][4] = "s/n"
            if (contador > 1 and (int(self.linhas[contador][0]) != int(self.linhas[contador-1][0])+1)):
                self.linhas[contador][0] = str(int(self.linhas[contador-1][0])+1)
        self.gravarArquivo()
        
if __name__ == '__main__':
    limpadorDeDados = LimpadorDeDados()
    limpadorDeDados.LimparDados()
    sys.exit()