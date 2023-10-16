from tkinter import *

from views.tela_inicial import TelaInicial

class TelaDeReinicio:
    def __init__(self, tela):
        self.tela = tela


    def comecarNovoJogo(self):
        novaTela = Tk()
        telaInicial = TelaInicial(novaTela)
        self.tela.destroy()