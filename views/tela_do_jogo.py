import random
from tkinter import *


class TelaDoJogo:

    # Tamanho padrão de casas
    tamanhoDaCasa = 28

    def __init__(self, linhas, colunas, bombas, root):
        self.qtdBandeiras = 0
        self.perdeu = False
        self.root = root
        self.linhas = linhas
        self.colunas = colunas
        self.bombas = bombas
        self.jogou = False
        self.matrizDoJogo = []
        self.casasRandomicas = []
        self.root.title('Campo Minado')
        self.x = self.linhas * self.tamanhoDaCasa
        self.y = self.colunas * self.tamanhoDaCasa
        self.criarTabuleiro()
        self.adicionarBombas()

    def criarTabuleiro(self):
        self.root.geometry(f"{self.x}x{self.y}")

        for linha in range(self.linhas):
            linhas = []
            for coluna in range(self.colunas):
                casa = Button(self.root)
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

    def calcularBombasAdjacentes(self, x, y):
        qtdBombasPerto = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.linhas and 0 <= y + j < self.colunas:
                    if self.casasRandomicas[x + i][y + j] == True:
                        qtdBombasPerto += 1
        return qtdBombasPerto

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
        # print(f'Casa verificada: {xX},{yY} \t tem bomba? {self.casasRandomicas[xX][yY]}')
        if self.casasRandomicas[xX][yY] == False:
           vizinhos = self.calcularBombasAdjacentes(yY, xX) 
           casaEspecifica['text'] = str(vizinhos)


        minado = self.casasRandomicas[xX][yY]
        if (minado):
            casaEspecifica['text'] = "B"
            self.revelarBombas()
            janelaPerdeu = Toplevel(self.root)
            janelaPerdeu.title("Você perdeu")
            janelaPerdeu.geometry("300x200")

            def voltar():
                janelaPerdeu.destroy()
            Label(janelaPerdeu, text="Infelizmente você encontrou uma bomba").pack()
            Button(janelaPerdeu, text="Voltar", command=voltar).pack()

    def jogar(self):
        self.root.mainloop()

    def encerrarJogo(self):
        self.root.destroy()
