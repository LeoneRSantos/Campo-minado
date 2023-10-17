import pytest
from jogo.dificuldade import Dificuldade
from main import main
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial
from tkinter import *

tela = Tk()

def teste_nivel_a_Escolher():
    assert Dificuldade.nivel == ''


def teste_Tamanho_Da_Casa():
    assert TelaDoJogo.tamanhoDaCasa == 28


def teste_Nivel_Escolhido():
    assert main != ''


def teste_Escolher_Nivel_Facil():
    d = Dificuldade('fácil')

    assert d.escolherNivel() == 'fácil'


def teste_Escolher_Facil_Pelo_Clique():
    d = Dificuldade('fácil')

    TelaInicial.dificuldade = 'fácil'

    assert d.nivel == TelaInicial.dificuldade


def teste_Escolher_Inter_Pelo_Clique():
    d = Dificuldade('intermediário')

    TelaInicial.dificuldade = 'intermediário'

    assert d.nivel == TelaInicial.dificuldade


def teste_Escolher_Dificil_Pelo_Clique():
    d = Dificuldade('difícil')

    TelaInicial.dificuldade = 'difícil'

    assert d.nivel == TelaInicial.dificuldade


def testar_Se_Comeca_Com_Menu():
    v = TelaInicial.comecar

    assert TelaInicial.indicarComeco() != v


def teste_Escolher_Nivel_Intermediário():
    d = Dificuldade('intermediário')

    assert d.escolherNivel() == 'intermediário'


def teste_Escolher_Nivel_Dificil():
    d = Dificuldade('difícil')

    assert d.escolherNivel() == 'difícil'


def testar_Dimensoes_Do_Facil():
    t = TelaDoJogo(8, 8, 10, tela)

    assert t.linhas == 8 and t.colunas == 8


def testar_Tabuleiro_Vazio_No_Facil():
    t = TelaDoJogo(8, 8, 10,tela)

    assert t.jogou == False


def testar_Marcacao_Facil():
    t = TelaDoJogo(8, 8, 10,tela)

    assert t.casasRandomicas[2][2] == True or t.casasRandomicas[2][2] == False


def testar_Marcacao_Dentr_oDo_Tabuleiro_Facil():
    t = TelaDoJogo(8, 8, 10,tela)

    for i in range(t.linhas):
        for c in range(t.colunas):
            assert t.casasRandomicas[i][c] == True or t.casasRandomicas[i][c] == False


def testar_Dimensoes_Intermediario():
    t = TelaDoJogo(10,16,30,tela) 

    contLinhas = 0
    contColunas = 0

    for l in range(t.linhas):
        contLinhas = l+1
        for c in range(t.colunas):
            contColunas = c+1

    assert contLinhas == 10 and contColunas == 16 

def testar_Tabuleiro_Vazio_No_Intermediario():
    t = TelaDoJogo(10, 16, 30,tela)

    assert t.jogou == False

def testar_Marcacao_Dentro_Do_Tabuleiro_Intermediario():
    t = TelaDoJogo(10, 16, 30,tela)

    for i in range(t.linhas):
        for c in range(t.colunas):
            assert t.casasRandomicas[i][c] == True or t.casasRandomicas[i][c] == False

def testar_Marcacao_Intermediario():
    t = TelaDoJogo(10, 16, 30,tela)

    assert t.casasRandomicas[8][10] == True or t.casasRandomicas[8][10] == False

def testar_Dimensoes_Dificil():
    t = TelaDoJogo(24,24,100,tela) 

    contLinhas = 0
    contColunas = 0

    for l in range(t.linhas):
        contLinhas = l+1
        for c in range(t.colunas):
            contColunas = c+1

    assert contLinhas == 24 and contColunas == 24 

def testar_Tabuleiro_Vazio_No_Dificil():
    t = TelaDoJogo(24, 24, 100,tela)

    assert t.jogou == False

def testar_Marcacao_Dificil():
    t = TelaDoJogo(24, 24, 100,tela)

    assert t.casasRandomicas[12][5] == True or t.casasRandomicas[12][5] == False