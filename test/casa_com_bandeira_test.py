from tkinter import *

from views.tela_do_jogo import TelaDoJogo

# Não deve ser possível descobrir uma zona que tenha uma bandeira. O jogador deve ser notificado se tentar fazê-lo.
# Testar se o jogador é informado em caso de descobrir uma zona que tenha bandeira
# Testar se ao tentar descobrir uma zona com bandeira, o tabuleiro permanece inalterado

tela = Tk()


def testar_informar_jogador():

    t = TelaDoJogo(8, 8, 10, tela)
    informa = False
    t.adicionarBandeira(2, 2)

    if t.matrizDoJogo[2][2]['text'] == 'P':
        informa = True

    assert informa == True and t.clique == True


def testar_se_tabuleiro_permanece_inalterado():

    t = TelaDoJogo(8, 8, 10, tela)
    t.adicionarBandeira(0, 0)
    inalterado = False

    for l in range(1, 7):
        for c in range(1, 7):
            if t.matrizDoJogo[l][c]['text'] == '':
                inalterado = True

    assert t.matrizDoJogo[0][0]['text'] == 'P' and inalterado == True
