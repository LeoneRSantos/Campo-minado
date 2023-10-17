from tkinter import * 
from views.tela_do_jogo import TelaDoJogo

# O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
# O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona. 

tela = Tk()

def testar_marcar_uma_zona_com_bandeira_facil():
    t = TelaDoJogo(8,8,10,tela)
    casa = Button(tela)

    t.adicionarBandeira(casa)

    assert t.qtdBandeiras > 0

def testar_marcar_uma_zona_com_bandeira_Intermediario():
    t = TelaDoJogo(10,16,30,tela)
    casa = Button(tela)

    t.adicionarBandeira(casa)

    assert t.qtdBandeiras > 0

def testar_marcar_uma_zona_com_bandeira_Dificil():
    t = TelaDoJogo(24,24,100,tela)
    casa = Button(tela)

    t.adicionarBandeira(casa)

    assert t.qtdBandeiras > 0

def testar_zona_coberta_facil():
    t = TelaDoJogo(8,8,10,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True

def testar_zona_coberta_Intermediario():
    t = TelaDoJogo(10,16,30,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True

def testar_zona_coberta_dificil():
    t = TelaDoJogo(24,24,100,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert coberto == True

def testar_zona_descoberta_facil():
    t = TelaDoJogo(8,8,10,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False

def testar_zona_descoberta_intermediario():
    t = TelaDoJogo(10,16,30,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False

def testar_zona_descoberta_dificil():
    t = TelaDoJogo(24,24,30,tela) 
    coberto = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.matrizDoJogo[l][c]['text'] != '':
                coberto = False

    assert not coberto == False

def testar_remover_bandeira_facil():
    t = TelaDoJogo(8,8,10,tela)
    casa = Button(tela)
    casa2 = Button(tela)

    t.adicionarBandeira(casa)
    t.adicionarBandeira(casa2)

    t.removerBandeira(casa)

    assert t.qtdBandeiras == 1

def testar_remover_bandeira_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    casa = Button(tela)
    casa2 = Button(tela)

    t.adicionarBandeira(casa)
    t.adicionarBandeira(casa2)

    t.removerBandeira(casa)

    assert t.qtdBandeiras == 1

def testar_remover_bandeira_dificil():
    t = TelaDoJogo(24,24,100,tela)
    casa = Button(tela)
    casa2 = Button(tela)

    t.adicionarBandeira(casa)
    t.adicionarBandeira(casa2)

    t.removerBandeira(casa)

    assert t.qtdBandeiras == 1

def testar_posicao_clicada_facil():
    t = TelaDoJogo(8,8,10,tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True

def testar_posicao_clicada_intermediario():
    t = TelaDoJogo(10,16,30,tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True

def testar_posicao_clicada_dificil():
    t = TelaDoJogo(24,24,100,tela)
    clique = True

    for l in range(t.linhas):
        for c in range(t.colunas):
            if t.casasRandomicas[l][c] == True or t.casasRandomicas[l][c] == False:
                clique = True
            else:
                clique = False

    assert clique == True