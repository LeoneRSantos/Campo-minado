from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# Testar se o tabuleiro é gerado

def testar_geracao_do_tabuleiro_facil():
   tf = TelaDoJogo(8,8,10,tela)
   area = 0

   for l in range(tf.linhas):
      for c in range(tf.colunas):
         area +=1

   assert tf.jogoIniciado == True and area == 64

def testar_geracao_do_tabuleiro_Intermediario():
   ti = TelaDoJogo(10,16,30,tela)
   area = 0

   for l in range(ti.linhas):
      for c in range(ti.colunas):
         area += 1
   
   assert ti.jogoIniciado == True and area == 160

def testar_geracao_do_tabuleiro_Dificil():
   td = TelaDoJogo(24,24,100,tela)
   area = 0

   for l in range(td.linhas):
      for c in range(td.colunas):
         area += 1

   assert td.jogoIniciado == True and area == 576