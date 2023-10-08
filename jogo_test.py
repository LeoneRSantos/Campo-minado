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
