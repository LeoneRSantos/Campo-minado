import pytest
from jogo.dificuldade import Dificuldade
from main import main
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial
from tkinter import *

tela = Tk()


def teste_nivel_a_Escolher():
    assert Dificuldade.nivel == ''


def teste_Escolher_Nivel_Facil():
    d = Dificuldade('fácil')

    assert d.escolherNivel() == d.nivel


def teste_Escolher_Nivel_Intermediario():
    d = Dificuldade('intermediário')

    assert d.escolherNivel() == d.nivel


def teste_Escolher_Nivel_dificil():
    d = Dificuldade('difícil')

    assert d.escolherNivel() == d.nivel


def testar_Se_Comeca_Com_Menu():
    TelaInicial.indicarComeco()

    assert TelaInicial.comecar == True


def teste_Escolher_Facil_Pelo_Clique():
    c = TelaInicial.comecar
    TelaInicial.indicarComeco()

    TelaInicial.dificuldade = 'fácil'
    d = Dificuldade(TelaInicial.dificuldade)

    assert d.escolherNivel() == TelaInicial.retornarDificuldade() and c == True


def teste_Escolher_Intermediario_Pelo_Clique():
    TelaInicial.indicarComeco()

    TelaInicial.dificuldade = 'fácil'
    d = Dificuldade(TelaInicial.dificuldade)

    assert d.escolherNivel() == TelaInicial.retornarDificuldade(
    ) and TelaInicial.comecar == True


def teste_Escolher_Dificil_Pelo_Clique():
    TelaInicial.indicarComeco()
    TelaInicial.dificuldade = 'difícil'

    d = Dificuldade(TelaInicial.dificuldade)

    assert d.escolherNivel() == TelaInicial.retornarDificuldade(
    ) and TelaInicial.comecar == False


def testar_Dimensoes_Do_Facil():
    t = TelaDoJogo(8, 8, 10, tela)
    area = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            area += 1

    assert t.linhas == 8 and t.colunas == 8 and area == 64


def testar_Dimensoes_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    area = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            area += 1

    assert t.linhas == 10 and t.colunas == 16 and area == 160


def testar_Dimensoes_Dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    area = 0

    for l in range(t.linhas):
        for c in range(t.colunas):
            area += 1

    assert t.linhas == 24 and t.colunas == 24 and area == 576


def testar_Tabuleiro_Vazio_No_Facil():
    t = TelaDoJogo(8, 8, 10, tela)
    vazio = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] == str(int):
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'B':
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'P':
                vazio = False

    assert vazio == True


def testar_Tabuleiro_Vazio_No_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    vazio = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] == str(int):
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'B':
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'P':
                vazio = False

    assert vazio == True


def testar_Tabuleiro_Vazio_No_Dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    vazio = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] == str(int):
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'B':
                vazio = False
            elif t.matrizDoJogo[l][c]['text'] == 'P':
                vazio = False

    assert vazio == True


def testar_Marcacao_Facil():
    t = TelaDoJogo(8, 8, 10, tela)

    listaPossibilidades = ['0', '2', '3', '4', 'B', 'P']

    for c in range(len(listaPossibilidades)):
        t.matrizDoJogo[2][2]['text'] = listaPossibilidades[c]

    assert t.matrizDoJogo[2][2]['text'] != ''


def testar_Marcacao_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)

    listaPossibilidades = ['0', '2', '3', '4', 'B', 'P']

    for c in range(len(listaPossibilidades)):
        t.matrizDoJogo[8][14]['text'] = listaPossibilidades[c]

    assert t.matrizDoJogo[8][14]['text'] != ''


def testar_Marcacao_Dificil():
    t = TelaDoJogo(24, 24, 100, tela)

    listaPossibilidades = ['0', '2', '3', '4', 'B', 'P']

    for c in range(len(listaPossibilidades)):
        t.matrizDoJogo[22][20]['text'] = listaPossibilidades[c]

    assert t.matrizDoJogo[22][20]['text'] != ''
