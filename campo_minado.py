#!/usr/bin/env python3
from tkinter import *
from views.tela_inicial import TelaInicial

def main():
    tela = Tk()
    t = TelaInicial(tela) 
    t.iniciarJogo()
   

if __name__ == '__main__':
    main()