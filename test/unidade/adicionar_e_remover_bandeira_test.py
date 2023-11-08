from tkinter import *
from views.tela_do_jogo import TelaDoJogo

# O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
# O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona.

tela = Tk()


def testar_marcar_uma_zona_com_bandeira_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    casa = Button(tela)

    t.adicionarBandeira(0, 2)

    assert t.qtdBandeiras > 0


def testar_marcar_uma_zona_com_bandeira_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    casa = Button(tela)

    t.adicionarBandeira(0, 5)

    assert t.qtdBandeiras > 0


def testar_marcar_uma_zona_com_bandeira_Dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    casa = Button(tela)

    t.adicionarBandeira(2, 2)

    assert t.qtdBandeiras > 0


def testar_zona_coberta_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True


def testar_zona_coberta_Intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True


def testar_zona_coberta_dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True


def testar_zona_descoberta_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False


def testar_zona_descoberta_intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False


def testar_zona_descoberta_dificil():
    t = TelaDoJogo(24, 24, 30, tela)
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False


def testar_remover_bandeira_facil():
    t = TelaDoJogo(8, 8, 10, tela)

    t.adicionarBandeira(0, 2)
    t.adicionarBandeira(1, 4)
    t.adicionarBandeira(0, 2)

    assert t.qtdBandeiras == 1


def testar_remover_bandeira_intermediario():
    t = TelaDoJogo(10, 16, 30, tela)

    t.adicionarBandeira(0, 2)
    t.adicionarBandeira(1, 4)
    t.adicionarBandeira(0, 2)

    assert t.qtdBandeiras == 1


def testar_remover_bandeira_dificil():
    t = TelaDoJogo(24, 24, 100, tela)

    t.adicionarBandeira(0, 2)
    t.adicionarBandeira(1, 4)
    t.adicionarBandeira(0, 2)

    assert t.qtdBandeiras == 1


def testar_posicao_clicada_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True


def testar_posicao_clicada_intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True


def testar_posicao_clicada_dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True


def testar_se_a_zona_clicada_tem_bandeira_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(0, 2)

    if t.matrizDoJogo[0][2]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True


def testar_se_a_zona_clicada_tem_bandeira_intermediario():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(0, 2)

    if t.matrizDoJogo[0][2]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True


def testar_se_a_zona_clicada_tem_bandeira_dificil():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(0, 2)

    if t.matrizDoJogo[0][2]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True


def testar_se_a_zona_clicada_esta_descoberta_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    descoberta = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    descoberta = True
            if t.casasRandomicas[l][c] == False:
                if t.matrizDoJogo[l][c]['text'] == str(int):
                    descoberta = True

    assert descoberta == False


def testar_se_a_zona_clicada_esta_descoberta_intermediario():
    t = TelaDoJogo(10, 16, 30, tela)
    descoberta = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    descoberta = True
            if t.casasRandomicas[l][c] == False:
                if t.matrizDoJogo[l][c]['text'] == str(int):
                    descoberta = True

    assert descoberta == False


def testar_se_a_zona_clicada_esta_descoberta_dificil():
    t = TelaDoJogo(24, 24, 100, tela)
    descoberta = False

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True:
                if t.matrizDoJogo[l][c]['text'] == 'B':
                    descoberta = True
            if t.casasRandomicas[l][c] == False:
                if t.matrizDoJogo[l][c]['text'] == str(int):
                    descoberta = True

    assert descoberta == False


def testar_se_a_zona_foi_marcada_com_bandeira_apos_clique_facil():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(3, 4)

    if t.matrizDoJogo[3][4]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True and t.qtdBandeiras > 0


def testar_se_a_zona_foi_marcada_com_bandeira_apos_clique_intermediario():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(3, 4)

    if t.matrizDoJogo[3][4]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True and t.qtdBandeiras > 0


def testar_se_a_zona_foi_marcada_com_bandeira_apos_clique_dificil():
    t = TelaDoJogo(8, 8, 10, tela)
    casaTemBandeira = False

    t.adicionarBandeira(3, 4)

    if t.matrizDoJogo[3][4]['text'] == 'P':
        casaTemBandeira = True

    assert casaTemBandeira == True and t.qtdBandeiras > 0
