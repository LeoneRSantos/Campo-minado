from tkinter import *
from views.tela_inicial import TelaInicial

tela = Tk()
# Deve ser possível começar com uma tela de escolha de nível de dificuldade.


def testar_se_a_tela_inicial_e_criada():
    telaDoInicio = TelaInicial(tela)

    telaDoInicio.indicarComeco()

    assert telaDoInicio.comeco == True


def testar_se_a_tela_mostra_o_nivel_facil():
    telaDoInicio = TelaInicial(tela)
    contem = False

    if 'fácil' in telaDoInicio.listaDeNiveis:
        contem = True

    assert contem == True

def testar_se_a_tela_mostra_o_nivel_intermediario():
    telaDoInicio = TelaInicial(tela)
    contem = False

    if 'intermediário' in telaDoInicio.listaDeNiveis:
        contem = True

    assert contem == True

def testar_se_a_tela_mostra_o_nivel_dificil():
    telaDoInicio = TelaInicial(tela)
    contem = False

    if 'difícil' in telaDoInicio.listaDeNiveis:
        contem = True

    assert contem == True

def testar_se_e_possivel_escolher_facil():
    telaDoInicio = TelaInicial(tela)
    telaDoInicio.indicarComeco()
    telaDoInicio.dificuldade = telaDoInicio.listaDeNiveis[0]

    telaDoInicio.escolherDificuldade(telaDoInicio.listaDeNiveis[0])

    assert telaDoInicio.retornarDificuldade() == 'fácil'

def testar_se_e_possivel_escolher_intermediario():
    telaDoInicio = TelaInicial(tela)
    telaDoInicio.indicarComeco()
    telaDoInicio.dificuldade = telaDoInicio.listaDeNiveis[1]

    telaDoInicio.escolherDificuldade(telaDoInicio.listaDeNiveis[1])

    assert telaDoInicio.retornarDificuldade() == 'intermediário'

def testar_se_e_possivel_escolher_dificil():
    telaDoInicio = TelaInicial(tela)
    telaDoInicio.indicarComeco()
    telaDoInicio.dificuldade = telaDoInicio.listaDeNiveis[2]

    telaDoInicio.escolherDificuldade(telaDoInicio.listaDeNiveis[2])

    assert telaDoInicio.retornarDificuldade() == 'difícil'
