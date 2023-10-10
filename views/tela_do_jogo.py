import random
import emoji
from tkinter import *


class TelaDoJogo:
    tela = Tk()

    # Tamanho padrão de casas
    tamanhoDaCasa = 28

    def __init__(self, linhas, colunas, bombas):
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.jogou = False
        self.matrizDoJogo = []
        self.casasRandomicas = []
        self.tela.title('Campo Minado')
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

        for linhaAtual in range(len(self.matrizDoJogo)):
            for colunaAtual in range(len(self.matrizDoJogo[linhaAtual])):
                if self.matrizDoJogo[linhaAtual][colunaAtual] == casaEspecifica:
                    xX = colunaAtual
                    yY = linhaAtual
        self.jogou = True
        # print(f'Casa verificada: {xX},{yY} \t tem bomba? {casasRandomicas[xX][yY]}')

        minado = self.casasRandomicas[xX][yY]
        if (minado):
            casaEspecifica['text'] = "B"
            self.revelarBombas()
            # emoji.emojize(":bomb:")

    def jogar(self):
        self.tela.mainloop()
