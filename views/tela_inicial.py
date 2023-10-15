from tkinter import *
from jogo.dificuldade import Dificuldade
from views.tela_do_jogo import TelaDoJogo


class TelaInicial:
    t = Tk()
    dificuldade = ''
    comecar = False

    def __init__(self,tela):
        self.tela = tela
        self.tela.title('Campo Minado')
        self.iniciarJogo()

    def escolherDificuldade(self, nivel):
        if (nivel == 'fácil'):
            d = Dificuldade('fácil') 
            TelaInicial.auxDificuldade = nivel

            d.escolherNivel()

        elif (nivel == 'intermediário'):
            d = Dificuldade('intermediário')
            TelaInicial.auxDificuldade = nivel

            d.escolherNivel()

        elif (nivel == 'difícil'):
            d = Dificuldade('difícil')
            TelaInicial.auxDificuldade = nivel

            d.escolherNivel()

    def escolherFacil(self):
        TelaInicial.dificuldade = 'fácil' 

        t = TelaDoJogo(8,8,10, self.tela)
        t.jogar()
        self.tela.destroy()

        self.escolherDificuldade(TelaInicial.dificuldade)

    def escolherIntermediario(self):
        self.dificuldade = 'intermediário'

        t = TelaDoJogo(16,10,30, self.tela)
        t.jogar()

        self.escolherDificuldade(self.dificuldade)

    def escolherDificil(self):
        self.dificuldade = 'difícil'

        t = TelaDoJogo(24,24,100,self.tela)
        t.jogar()

        self.escolherDificuldade(self.dificuldade)

    @staticmethod
    def retornarDificuldade():
        return TelaInicial.dificuldade 
    
    @staticmethod
    def indicarComeco(): 
        if TelaInicial.comecar == False:
            TelaInicial.comecar = True
        else: 
            TelaInicial.comecar = False

    def iniciarJogo(self):
        TelaInicial.indicarComeco()

        self.t.geometry('300x200')

        facil = Button(self.t, text='Fácil', command=self.escolherFacil)
        facil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        intermediario = Button(self.t, text='Intermediário',
                               command=self.escolherIntermediario)
        intermediario.pack(fill=BOTH, expand=True, padx=8, pady=8)

        dificil = Button(self.t, text='Difícil', command=self.escolherDificil)
        dificil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        TelaInicial.indicarComeco()

        self.t.mainloop()
