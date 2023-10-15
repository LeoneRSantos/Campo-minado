from tkinter import *
from views.tela_inicial import TelaInicial

def main():
    t = TelaDoJogo(8,8,10) 
    t.jogar()
    # t = TelaInicial('Fácil') 
    # t.iniciarJogo()
   

if __name__ == '__main__':
    main()