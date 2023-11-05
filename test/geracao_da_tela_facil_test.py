from tkinter import *
from views.tela_do_jogo import TelaDoJogo
from views.tela_inicial import TelaInicial
from unittest.mock import Mock

tela = Tk()
telaInicial = TelaInicial(tela)


def testar_geracao_da_tela_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    geracao = Mock(side_effect=tf.jogar)

    geracao.assert_called_once_with
