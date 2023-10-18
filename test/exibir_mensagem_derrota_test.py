from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# O software deve fornecer uma mensagem de derrota quando uma área com bomba for descoberta.

tela = Tk() 

def testar_exibir_mensagem_facil():
    tf = TelaDoJogo(8,8,10,tela)

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                tf.verificarCasa(tf.matrizDoJogo[l][c])

    assert tf.perdeu == True

def testar_exibir_mensagem_dificil():
    tf = TelaDoJogo(24,24,100,tela)

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                tf.verificarCasa(tf.matrizDoJogo[l][c])

    assert tf.perdeu == True
   