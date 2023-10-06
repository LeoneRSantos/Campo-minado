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

    matrizDoJogo = []
    # Casas randomizadas
    casasRandomicas = []

    # Função para verificar a casa
    def verificarCasa(casaEspecifica):
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




