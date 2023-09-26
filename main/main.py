from jogo.jogo import Dificuldade
from jogo.tabuleiro import Tabuleiro

def main():
    d = Dificuldade('difícil')
    t = Tabuleiro(d.nivel)
    t.iniciarTabuleiro()
    t.mostrarTabuleiro()
   

if __name__ == '__main__':
    main()