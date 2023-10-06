from jogo.dificuldade import Dificuldade
from jogo.tabuleiro import Tabuleiro
from views.interface import TelaDoJogo

def main():
    # d = Dificuldade('difícil')
    # t = Tabuleiro(d.nivel)
    # t.iniciarTabuleiro()
    # t.mostrarTabuleiro()
    t = TelaDoJogo() 
    t.jogar()
   

if __name__ == '__main__':
    main()