from tkinter import Tk
from views.tela_do_jogo import TelaDoJogo

tela = Tk()


# Verificar se as zonas estão todas cobertas 
# Verificar se nenhuma zona tem bandeira 

def testar_zonas_cobertas_facil():
    t = TelaDoJogo(8,8,10,tela)

    assert t.jogou == False

def testar_zonas_cobertas_intermediario():
    t = TelaDoJogo(10,16,30,tela)

    assert t.jogou == False

def testar_zonas_cobertas_Dificil():
    t = TelaDoJogo(24,24,100,tela)

    assert t.jogou == False

def testar_se_nenhuma_casa_tem_bandeira_Facil():
    t = TelaDoJogo(8,8,10,tela)

    assert t.qtdBandeiras == 0

def testar_se_nenhuma_casa_tem_bandeira_Intermediario():
    t = TelaDoJogo(10,16,30,tela)

    assert t.qtdBandeiras == 0

def testar_se_nenhuma_casa_tem_bandeira_Dificil():
    t = TelaDoJogo(24,24,100,tela)

    assert t.qtdBandeiras == 0