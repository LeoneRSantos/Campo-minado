from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# O jogo deve continuar até que uma bomba seja encontrada.

tela = Tk()

def testar_se_o_jogo_para_ao_encontrar_bomba_facil():
    tf = TelaDoJogo(8,8,10,tela) 
    para = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                tf.verificarCasa(tf.matrizDoJogo[l][c])

                if tf.matrizDoJogo[l][c]['state'] == "disabled":
                    para = True

    assert para == True


def testar_se_o_jogo_para_ao_encontrar_bomba_dificil():
    td = TelaDoJogo(24,24,100,tela) 
    para = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                td.verificarCasa(td.matrizDoJogo[l][c])

                if td.matrizDoJogo[l][c]['state'] == "disabled":
                    para = True

    assert para == True

    
def testar_se_o_jogo_para_ao_encontrar_bomba_intermediario():
    ti = TelaDoJogo(10,16,30,tela) 
    para = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                if ti.matrizDoJogo[l][c]['state'] == "disabled":
                    para = True

    assert para == False