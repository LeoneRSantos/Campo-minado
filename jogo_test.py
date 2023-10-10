import pytest
from jogo.dificuldade import Dificuldade
from main import main
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial


def testeNivelAEscolher():
    assert Dificuldade.nivel == ''


def testeTamanhoDaCasa():
    assert TelaDoJogo.tamanhoDaCasa == 28


def testeNivelEscolhido():
    assert main != ''


def testeEscolherNivelFacil():
    d = Dificuldade('fácil')

    assert d.escolherNivel() == 'fácil'


def testeEscolherFacilPeloClique():
    d = Dificuldade('fácil')

    TelaInicial.dificuldade = 'fácil'

    assert d.nivel == TelaInicial.dificuldade


def testeEscolherInterPeloClique():
    d = Dificuldade('intermediário')

    TelaInicial.dificuldade = 'intermediário'

    assert d.nivel == TelaInicial.dificuldade


def testeEscolherDificilPeloClique():
    d = Dificuldade('difícil')

    TelaInicial.dificuldade = 'difícil'

    assert d.nivel == TelaInicial.dificuldade


def testarSeComecaCoMenu():
    v = TelaInicial.comecar

    assert TelaInicial.indicarComeco() != v


def testeEscolherNivelIntermediário():
    d = Dificuldade('intermediário')

    assert d.escolherNivel() == 'intermediário'


def testeEscolherNiveDificil():
    d = Dificuldade('difícil')

    assert d.escolherNivel() == 'difícil'


def testarDimensoesDoFacil():
    t = TelaDoJogo(8, 8, 10)

    assert t.linhas == 8 and t.colunas == 8


def testarTabuleiroVazioNoFacil():
    t = TelaDoJogo(8, 8, 10)

    assert t.jogou == False


def testarMarcacaoFacil():
    t = TelaDoJogo(8, 8, 10)

    assert t.casasRandomicas[2][2] == True or t.casasRandomicas[2][2] == False


def testarMarcacaoDentroDoTabuleiroFacil():
    t = TelaDoJogo(8, 8, 10)

    for i in range(t.linhas):
        for c in range(t.colunas):
            assert t.casasRandomicas[i][c] == True or t.casasRandomicas[i][c] == False


def testarDimensoesIntermediario():
    t = TelaDoJogo(10,16,30) 

    contLinhas = 0
    contColunas = 0

    for l in range(t.linhas):
        contLinhas = l+1
        for c in range(t.colunas):
            contColunas = c+1

    assert contLinhas == 10 and contColunas == 16 

def testarTabuleiroVazioNoIntermediario():
    t = TelaDoJogo(10, 16, 30)

    assert t.jogou == False

def testarMarcacaoDentroDoTabuleiroIntermediario():
    t = TelaDoJogo(10, 16, 30)

    for i in range(t.linhas): 
        for c in range(t.colunas): 
            assert t.casasRandomicas[i][c] == True or t.casasRandomicas[i][c]==False