from tkinter import *
from unittest.mock import Mock
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

#   - [ ] Testar se a mensagem de derrota é criada.
#   - [ ] Verificar se ela informa que o jogador perdeu por encontrar uma bomba.
#   - [ ] Testar se ela se sobrepõe a tela anterior.
#   - [ ] Testar se ela é criada separadamente.
#   - [ ] Testar se, ao criar a nova tela, a tela anterior é interrompida.
# #   - [ ] Testar se ao fechar a tela de mensagem de derrota, a tela do tabuleiro também é fechada.
#   - [ ] Testar se as demais casas ainda não descobertas são descobertas após encontrar uma bomba.


def testar_se_a_tela_de_derrota_e_criada_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    perdeu = Toplevel(tf.root)

    facil = Mock(spec=perdeu.title("Você perdeu"))

    facil.assert_called


def testar_se_a_tela_de_derrota_e_criada_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    perdeu = Toplevel(ti.root)

    medio = Mock(spec=perdeu.title("Você perdeu"))

    medio.assert_called


def testar_se_a_tela_de_derrota_e_criada_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    perdeu = Toplevel(td.root)

    dificil = Mock(spec=perdeu.title("Você perdeu"))

    dificil.assert_called


def testar_se_a_tela_se_sobrepoe_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    facil = Mock(spec=Toplevel(tf.root))

    facil.assert_called


def testar_se_a_tela_se_sobrepoe_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    medio = Mock(spec=Toplevel(ti.root))

    medio.assert_called


def testar_se_a_tela_se_sobrepoe_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    dificil = Mock(spec=Toplevel(td.root))

    dificil.assert_called


def testar_se_a_tela_informa_da_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)

    facil = Mock(spec=Label(Toplevel(tf.root),
                 text="Infelizmente você encontrou uma bomba").pack())

    facil.assert_called


def testar_se_a_tela_informa_da_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)

    inter = Mock(spec=Label(Toplevel(ti.root),
                 text="Infelizmente você encontrou uma bomba").pack())

    inter.assert_called


def testar_se_a_tela_informa_da_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)

    facil = Mock(spec=Label(Toplevel(td.root),
                 text="Infelizmente você encontrou uma bomba").pack())

    facil.assert_called
