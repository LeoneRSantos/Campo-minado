from jogo.dificuldade import Dificuldade
from jogo.tabuleiro import Tabuleiro
from views.interface import TelaDoJogo

def main():
    t = TelaDoJogo(8,8,10) 
    t.jogar()
   

if __name__ == '__main__':
    main()