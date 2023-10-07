# from views.interface import TelaDoJogo
from views.tela_inicial import TelaInicial

def main():
    # t = TelaDoJogo(24,24,100) 
    # t.jogar()
    t = TelaInicial('Fácil') 
    t.iniciarJogo()
   

if __name__ == '__main__':
    main()