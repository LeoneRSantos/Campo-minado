import random
import emoji
from tkinter import *


class TelaDoJogo:
    tela = Tk()

    # tamanho do tabuleiro fácil
    tabuleiro = [8, 8]
    # Tamanho padrão de casas
    tamanhoDaCasa = 32

    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.matrizDoJogo = []
        self.casasRandomicas = []
        self.tela.title('Baiano')
        self.x = self.linhas * self.tamanhoDaCasa
        self.y = self.colunas * self.tamanhoDaCasa
        self.criarTabuleiro()
        self.adicionarBombas()

    def criarTabuleiro(self):
        self.tela.geometry(f"{self.x}x{self.y}")

        for linha in range(self.linhas):
            linhas = []
            for coluna in range(self.colunas):
                casa = Button(self.tela)
                casa['command'] = lambda casa=casa: self.verificarCasa(casa)
                posx = linha * self.tamanhoDaCasa
                posy = coluna * self.tamanhoDaCasa
                casa.place(x=posx, y=posy, width=self.tamanhoDaCasa,
                           height=self.tamanhoDaCasa)
                linhas.append(casa)
            self.matrizDoJogo.append(linhas)

    def revelarBombas(self):
        for linha in range(len(self.matrizDoJogo)):
            for coluna in range(len(self.matrizDoJogo[linha])):
                if self.casasRandomicas[linha][coluna]:
                    self.matrizDoJogo[linha][coluna]['text'] = "B"

    def adicionarBombas(self):
        self.casasRandomicas = [[False for _ in range(
            self.colunas)] for _ in range(self.linhas)]
        bombas_colocadas = 0

        while bombas_colocadas < self.bombas:
            x = random.randint(0, self.linhas - 1)
            y = random.randint(0, self.colunas - 1)

            if not self.casasRandomicas[x][y]:
                self.casasRandomicas[x][y] = True
                bombas_colocadas += 1

    # Função para verificar a casa
    def verificarCasa(self, casaEspecifica):
        xX = -1
        yY = -1

        for linhaAtual in range(len(TelaDoJogo.matrizDoJogo)): 
            for colunaAtual in range(len(TelaDoJogo.matrizDoJogo[linhaAtual])):
                if TelaDoJogo.matrizDoJogo[linhaAtual][colunaAtual] == casaEspecifica:
                    xX = colunaAtual
                    yY = linhaAtual
                
                
        # print(f'Casa verificada: {xX},{yY} \t tem bomba? {casasRandomicas[xX][yY]}')

        minado = TelaDoJogo.casasRandomicas[xX][yY]
        if(minado):
            casaEspecifica['text'] = '💣'
            print('💣')
            # emoji.emojize(":bomb:")
        

    # Geração do tabuleiro
    tela.geometry(f"{x}x{y}")

    for linha in range(tabuleiro[0]):
        linhas = []
        for coluna in range(tabuleiro[1]):

            casa = Button(tela) 
            casa['command'] = lambda casa = casa: TelaDoJogo.verificarCasa(casa)

            posx = linha*tamanhoDaCasa
            posy = coluna*tamanhoDaCasa
            casa.place(x=posx, y=posy, width=tamanhoDaCasa, height=tamanhoDaCasa) 
            linhas.append(casa)
        matrizDoJogo.append(linhas)

    for l in range(tabuleiro[0]):
        novoValor = []
        for c in range(tabuleiro[1]):
            temBomba = bool(random.randint(0,1))
            novoValor.append(temBomba)
        casasRandomicas.append(novoValor)
    print(casasRandomicas)


    def jogar(self):

        TelaDoJogo.tela.mainloop()




