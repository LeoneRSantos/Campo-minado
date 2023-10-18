from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# O software deve exibir o número de bandeiras disponíveis para uso.

tela = Tk()

def testar_numero_de_bandeiras_facil():
    t = TelaDoJogo(8,8,10,tela)
    
    for l in range(t.linhas):
        for c in range(t.colunas):
            t.adicionarBandeira(t.matrizDoJogo[l][c])

    assert t.qtdBandeiras == 10

def testar_numero_de_bandeiras_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    
    for l in range(t.linhas):
        for c in range(t.colunas):
            t.adicionarBandeira(t.matrizDoJogo[l][c])

    assert t.qtdBandeiras == 30

def testar_numero_de_bandeiras_dificil():
    t = TelaDoJogo(24,24,100,tela)
    
    for l in range(t.linhas):
        for c in range(t.colunas):
            t.adicionarBandeira(t.matrizDoJogo[l][c])

    assert t.qtdBandeiras == 100

def testar_se_o_numero_de_bandeiras_disponivel_e_exibido():
    tf = TelaDoJogo(8,8,10,tela)
    ti = TelaDoJogo(10,16,30,tela)
    td = TelaDoJogo(24,24,100,tela)
    
    assert tf.clique == True and ti.clique == True and td.clique == True