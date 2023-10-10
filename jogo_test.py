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
    t = TelaDoJogo(8,8,10)

    assert t.linhas == 8 and t.colunas == 8 

def testarTabuleiroVazioNoFacil(): 
    t = TelaDoJogo(8,8,10) 

    assert len(t.matrizDoJogo) == 8 and len(t.casasRandomicas) == 8

def testarMarcacao():
    t = TelaDoJogo(8,8,10)

    assert t.casasRandomicas[2][2] == True or t.casasRandomicas[2][2] == False  

def testarMarcacaoDentroDoTabuleiro(): 
    t = TelaDoJogo(8,8,10)

    for i in range(t.linhas): 
        for c in range(t.colunas): 
            assert t.casasRandomicas[i][c] == True or t.casasRandomicas[i][c]==False