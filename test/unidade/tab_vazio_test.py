from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk() 

# Testar se o tabuleiro é de tamanho vazio

def testar_se_o_tabuleiro_esta_vazio_Facil():
    t = TelaDoJogo(8,8,10,tela)
    
    assert not len(t.casasRandomicas) == 0

def testar_se_o_tabuleiro_esta_vazio_Intermediario():
    t = TelaDoJogo(10,16,30,tela)
    
    assert not len(t.casasRandomicas) == 0


def testar_se_o_tabuleiro_esta_vazio_Dificil():
    t = TelaDoJogo(24,24,100,tela)
    
    assert not len(t.casasRandomicas) == 0