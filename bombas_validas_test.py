from tkinter import Tk 
from views.tela_do_jogo import TelaDoJogo

# Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar)[x] 

tela = Tk()

def testar_bombas_validas_Facil():
    t = TelaDoJogo(8,8,10,tela)

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                assert not t.casasRandomicas == str


def testar_bombas_validas_Intermediario():
    t = TelaDoJogo(10,16,30,tela)

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                assert not t.casasRandomicas == str


def testar_bombas_validas_Dificil():
    t = TelaDoJogo(24,24,100,tela)

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                assert not t.casasRandomicas == str