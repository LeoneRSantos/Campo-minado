import random
from tkinter import *


class TelaDoJogo:

    # Tamanho padrão de casas
    tamanhoDaCasa = 28
    informar = False
    d = ''

    def __init__(self, linhas, colunas, bombas, root):
        self.jogoIniciado = False
        self.clique = False
        self.qtdBandeiras = 0
        self.perdeu = False
        self.venceu = False
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

    def adicionarBandeira(self, x, y):
        self.clique = True

        if self.qtdBandeiras > self.bombas:
            self.qtdBandeiras = self.bombas

        elif self.qtdBandeiras < self.bombas and self.matrizDoJogo[x][y]['text'] == '':
            self.matrizDoJogo[x][y]['text'] = 'P'
            self.matrizDoJogo[x][y]['fg'] = '#000C20'
            self.matrizDoJogo[x][y]['bg'] = '#F0EDE0'
            self.qtdBandeiras += 1
            print(f'Adicionar bandeira')

        elif self.matrizDoJogo[x][y]['text'] == 'P':
            self.matrizDoJogo[x][y]['text'] = ''
            self.qtdBandeiras -= 1

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
                casa['bg'] = '#E3E7F1'
                casa.bind('<Button-3>', lambda Event, x=linha,
                          y=coluna: self.adicionarBandeira(x, y))
                linhas.append(casa)
            self.matrizDoJogo.append(linhas)

        if self.linhas == 8:
            TelaDoJogo.d = 'fácil'
        elif self.linhas == 16:
            TelaDoJogo.d = 'intermediário'
        elif self.linhas == 24:
            TelaDoJogo.d = 'difícil'

        self.jogoIniciado = True

        tutorial = Toplevel(self.root)
        tutorial.title("Como jogar")
        tutorial.geometry("500x300")
        Label(
            tutorial, text=f'- Você escolheu o nível {TelaDoJogo.d}').pack(padx=8, pady=8, anchor="center")
        Label(tutorial, text=f'- Seu tabuleiro tem dimensões {self.colunas} x {self.linhas} e {self.bombas} bombas').pack(
            padx=8, pady=8, anchor="center")
        Label(tutorial, text=f'- Você pode adicionar uma bandeira no local que imaginar ter uma bomba.').pack(
            padx=8, pady=8, anchor="center")
        Label(tutorial, text=f'- Você tem um total de {self.bombas} bandeiras.').pack(
            padx=8, pady=8, anchor="center")
        Label(tutorial, text=f'- Para vencer o jogo, você deve marcar todos os pontos que têm bomba \ncom bandeiras.').pack(
            padx=8, pady=8, anchor="center")
        Label(tutorial, text=f'- Caso clique em um local com bomba, você perde.').pack(
            padx=8, pady=8, anchor="center")

    def revelarBombas(self):
        for linha in range(len(self.matrizDoJogo)):
            for coluna in range(len(self.matrizDoJogo[linha])):
                if self.casasRandomicas[linha][coluna]:
                    self.matrizDoJogo[linha][coluna]['text'] = "X"
                    self.matrizDoJogo[linha][coluna]['bg'] = '#970C10'

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

    def verificarVitoria(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if self.casasRandomicas[linha][coluna] == True:
                    if self.matrizDoJogo[linha][coluna]['text'] == 'P':
                        self.venceu = True
                        janelaVenceu = Toplevel(self.root)
                        janelaVenceu.title("Você venceu!")
                        janelaVenceu.geometry("300x200")

                        Label(
                            janelaVenceu, text="Parabéns! Você conseguiu vencer o jogo.").pack()

    def verificarCasa(self, casaEspecifica):
        xX = -1
        yY = -1

        self.verificarVitoria()

        for linhaAtual in range(len(self.matrizDoJogo)):
            for colunaAtual in range(len(self.matrizDoJogo[linhaAtual])):
                if self.matrizDoJogo[linhaAtual][colunaAtual] == casaEspecifica:
                    xX = linhaAtual
                    yY = colunaAtual
        self.jogou = True

        if self.casasRandomicas[xX][yY] == False:
            vizinhos = self.calcularBombasAdjacentes(xX, yY)
            casaEspecifica['text'] = str(vizinhos)
            casaEspecifica['fg'] = '#000C20'
            casaEspecifica['bg'] = '#F0EDE0'

            if vizinhos == 0:
                for l in range(-1, 2):
                    for c in range(-1, 2):
                        if 0 <= xX + l < self.linhas and 0 <= yY + c < self.colunas:
                            self.verificarCasa(
                                self.matrizDoJogo[xX + l][yY + c])
                            self.matrizDoJogo[xX + l][yY + c]['fg'] = '#000C20'
                            self.matrizDoJogo[xX + l][yY + c]['bg'] = '#F0EDE0'

        minado = self.casasRandomicas[xX][yY]
        if (minado):
            self.perdeu = True
            casaEspecifica['text'] = "X"
            self.revelarBombas()
            janelaPerdeu = Toplevel(self.root)
            janelaPerdeu.title("Você perdeu")
            janelaPerdeu.geometry("300x200")

            Label(janelaPerdeu, text="Infelizmente você encontrou uma bomba").pack()
            for linhaAtual in range(len(self.matrizDoJogo)):
                for colunaAtual in range(len(self.matrizDoJogo[linhaAtual])):
                    self.matrizDoJogo[linhaAtual][colunaAtual]['state'] = "disabled"

        if casaEspecifica['text'] == 'P':
            TelaDoJogo.informar = True

            casaBandeira = Toplevel(self.tela)
            casaBandeira.title("Casa com bandeira")
            casaBandeira.geometry("300x200")
            Label(casaBandeira, text="Esta casa tem bandeira. Você precisa remover a bandeira para poder descobrir a casa.").pack()

    def jogar(self):
        self.root.mainloop()
        self.jogoIniciado = True

        return bool(self.jogoIniciado)

    def encerrarJogo(self):
        self.root.destroy()
        self.jogoIniciado = False
