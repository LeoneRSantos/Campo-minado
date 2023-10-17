from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# Testar se o tabuleiro é gerado

def testar_geracao_do_tabuleiro_facil():
   t = TelaDoJogo(8,8,10,tela)

   assert len(t.casasRandomicas) > 0

def testar_geracao_do_tabuleiro_Intermediario():
   t = TelaDoJogo(10,16,30,tela)

   assert len(t.casasRandomicas) > 0

def testar_geracao_do_tabuleiro_Dificil():
   t = TelaDoJogo(24,24,100,tela)

   assert len(t.casasRandomicas) > 0