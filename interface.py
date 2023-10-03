import random
from tkinter import *

tela = Tk()

# tamanho do tabuleiro fácil
tabuleiro = [8, 8]
# Tamanho padrão de casas
tamanhoDaCasa = 32

tela.title("Campo Minado")
x = tabuleiro[0] * tamanhoDaCasa
y = tabuleiro[1] * tamanhoDaCasa

matrizDoJogo = []
# Casas randomizadas
casasRandomicas = []

# Função para verificar a casa
def verificarCasa(casaEspecifica):
    xX = -1
    yY = -1

    for linhaAtual in range(len(matrizDoJogo)): 
        for colunaAtual in range(len(matrizDoJogo[linhaAtual])):
            if matrizDoJogo[linhaAtual][colunaAtual] == casaEspecifica:
                xX = colunaAtual
                yY = linhaAtual
            
            
    # print(f'Casa verificada: {xX},{yY} \t tem bomba? {casasRandomicas[xX][yY]}')

    minado = casasRandomicas[xX][yY]
    if(minado):
        casaEspecifica['text'] = 'X'
    

# Geração do tabuleiro
tela.geometry(f"{x}x{y}")

for linha in range(tabuleiro[0]):
    linhas = []
    for coluna in range(tabuleiro[1]):

        casa = Button(tela) 
        casa['command'] = lambda casa = casa: verificarCasa(casa)

class Frame1(Frame):
    def __init__(self, ws):
        Frame.__init__(self, ws, bg="#006699")
        self.ws = ws
        self.widgets()

    def widgets(self):
        self.grid(row=0, column=0, padx=20, pady=20) # margins


class Win(Tk):

    def __init__(self, ws):
        Tk.__init__(self, ws)
        self.ws = ws
        self.title('Campo Minado')
        self.geometry('500x500')
        self.main()

    def main(self):
        self.w = Frame1(self)
        self.w.pack()

if __name__== "__main__":
    app = Win(None)
    app.mainloop()