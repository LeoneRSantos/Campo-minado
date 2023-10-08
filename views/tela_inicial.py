from tkinter import *
from jogo.dificuldade import Dificuldade


class TelaInicial:
    t = Tk()

    def __init__(self, dificuldade):
        self.t.title('Campo Minado')
        self.dificuldade = dificuldade
        self.iniciarJogo()

    def escolherDificuldade(self):
        if (self.dificuldade == 'fácil'):
            d = Dificuldade('fácil')

            d.escolherNivel()

        elif (self.dificuldade == 'intermediário'):
            d = Dificuldade('intermediário')

            d.escolherNivel()

        elif (self.dificuldade == 'difícil'):
            d = Dificuldade('difícil')

            d.escolherNivel()

    def escolherFacil(self):
        self.dificuldade = 'fácil'

        self.escolherDificuldade()

    def escolherIntermediario(self):
        self.dificuldade = 'intermediário'

        self.escolherDificuldade()

    def escolherDificil(self):
        self.dificuldade = 'difícil'

        print(self.dificuldade)

    def iniciarJogo(self):

        self.t.geometry('300x200')

        facil = Button(self.t, text='Fácil', command=self.escolherFacil)
        facil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        intermediario = Button(self.t, text='Intermediário',
                               command=self.escolherIntermediario)
        intermediario.pack(fill=BOTH, expand=True, padx=8, pady=8)

        dificil = Button(self.t, text='Difícil', command=self.escolherDificil)
        dificil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        self.t.mainloop()
