from tkinter import *
from jogo.dificuldade import Dificuldade
from views.tela_do_jogo import TelaDoJogo


class TelaInicial:

    def __init__(self, tela):
        self.tela = tela
        self.tela.title('Campo Minado')
        self.comeco = False
        self.clique = False
        self.dificuldade = ''
        self.listaDeNiveis = ['fácil', 'intermediário', 'difícil']

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
        TelaInicial.dificuldade = self.listaDeNiveis[0]
        self.clique = True

        t = TelaDoJogo(8, 8, 10, self.tela)
        t.jogar()
        self.tela.destroy()

        self.escolherDificuldade(TelaInicial.dificuldade)

    def escolherIntermediario(self):
        self.dificuldade = self.listaDeNiveis[1]
        self.clique = True

        t = TelaDoJogo(16, 10, 30, self.tela)
        t.jogar()

        self.escolherDificuldade(self.dificuldade)

    def escolherDificil(self):
        self.dificuldade = self.listaDeNiveis[2]
        self.clique = True

        t = TelaDoJogo(24, 24, 100, self.tela)
        t.jogar()

        self.escolherDificuldade(self.dificuldade)

    def retornarDificuldade(self):
        return self.dificuldade

    def indicarComeco(self):
        if self.comeco == False:
            self.comeco = True
        else:
            self.comeco = False

    def iniciarJogo(self):
        self.indicarComeco()

        self.tela.geometry('300x200')

        facil = Button(
            self.tela, text=self.listaDeNiveis[0].capitalize(), command=self.escolherFacil)
        facil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        intermediario = Button(self.tela, text=self.listaDeNiveis[1].capitalize(),
                               command=self.escolherIntermediario)
        intermediario.pack(fill=BOTH, expand=True, padx=8, pady=8)

        dificil = Button(self.tela, text=self.listaDeNiveis[2].capitalize(
        ), command=self.escolherDificil)
        dificil.pack(fill=BOTH, expand=True, padx=8, pady=8)

        self.indicarComeco()

        self.tela.mainloop()
