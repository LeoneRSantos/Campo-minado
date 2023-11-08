from tkinter import *
from views.tela_do_jogo import TelaDoJogo
from unittest.mock import Mock

tela = Tk()

# - [ ] Testar se a tela de tutorial informa o nível escolhido.
#   - [ ] Testar se a tela de tutorial informa as proporções do tabuleiro.
#   - [ ] Testar se a tela de tutorial informa a quantidade de bombas daquele nível.
#   - [ ] Testar se a tela de tutorial informa a quantidade de bandeiras daquele nível.
#   - [ ] Testar se a tela de tutorial informa como vencer o jogo.
#   - [ ] Testar se a tela de tutorial informa como se perde o jogo.

def testar_se_a_tela_informa_o_nivel_facil():
    tf = TelaDoJogo(8,8,10,tela)

    facil = Mock(spec=Label(
            Toplevel(tf.root), text=f'- Você escolheu o nível {TelaDoJogo.d}').pack(padx=8, pady=8, anchor="center"))

    facil.assert_called
    assert TelaDoJogo.d == 'fácil'

def testar_se_a_tela_informa_o_nivel_intermediario():
    ti = TelaDoJogo(16,10,30,tela)

    inter = Mock(spec=Label(
            Toplevel(ti.root), text=f'- Você escolheu o nível {TelaDoJogo.d}').pack(padx=8, pady=8, anchor="center"))

    inter.assert_called
    assert TelaDoJogo.d == 'intermediário'

def testar_se_a_tela_informa_o_nivel_dificil():
    td = TelaDoJogo(24,24,100,tela)

    dificil = Mock(spec=Label(
            Toplevel(td.root), text=f'- Você escolheu o nível {TelaDoJogo.d}').pack(padx=8, pady=8, anchor="center"))

    dificil.assert_called
    assert TelaDoJogo.d == 'difícil'

def testar_se_a_tela_informa_as_proporcoes_facil():
    tf = TelaDoJogo(8,8,10,tela)

    facil = Mock(spec=Label(Toplevel(tf.root), text=f'- Seu tabuleiro tem dimensões {tf.colunas} x {tf.linhas} e {tf.bombas} bombas').pack(
            padx=8, pady=8, anchor="center"))

    facil.assert_called
    assert tf.linhas == 8 and tf.colunas == 8

def testar_se_a_tela_informa_as_proporcoes_intermediario():
    ti = TelaDoJogo(10,16,30,tela)

    inter = Mock(spec=Label(Toplevel(ti.root), text=f'- Seu tabuleiro tem dimensões {ti.colunas} x {ti.linhas} e {ti.bombas} bombas').pack(
            padx=8, pady=8, anchor="center"))

    inter.assert_called
    assert ti.linhas == 10 and ti.colunas == 16

def testar_se_a_tela_informa_as_proporcoes_dificil():
    td = TelaDoJogo(24,24,100,tela)

    dificil = Mock(spec=Label(Toplevel(td.root), text=f'- Seu tabuleiro tem dimensões {td.colunas} x {td.linhas} e {td.bombas} bombas').pack(
            padx=8, pady=8, anchor="center"))

    dificil.assert_called
    assert td.linhas == 24 and td.colunas == 24


def testar_se_a_tela_informa_como_vencer_o_jogo_facil():
    tf = TelaDoJogo(8,8,10,tela)

    facil = Mock(spec=Label(Toplevel(tf.root), text=f'- Para vencer o jogo, você deve marcar todos os pontos que têm bomba \ncom bandeiras.').pack(
            padx=8, pady=8, anchor="center"))

    facil.assert_called

def testar_se_a_tela_informa_como_vencer_o_jogo_intermediario():
    ti = TelaDoJogo(10,16,30,tela)

    intermediario = Mock(spec=Label(Toplevel(ti.root), text=f'- Para vencer o jogo, você deve marcar todos os pontos que têm bomba \ncom bandeiras.').pack(
            padx=8, pady=8, anchor="center"))

    intermediario.assert_called

def testar_se_a_tela_informa_como_vencer_o_jogo_dificil():
    td = TelaDoJogo(24,24,100,tela)

    dificil = Mock(spec=Label(Toplevel(td.root), text=f'- Para vencer o jogo, você deve marcar todos os pontos que têm bomba \ncom bandeiras.').pack(
            padx=8, pady=8, anchor="center"))

    dificil.assert_called

def testar_se_a_tela_de_tutorial_informa_como_se_perde_o_jogo_facil():
    tf = TelaDoJogo(8,8,10,tela)

    facil = Mock(spec=Label(Toplevel(tf.root), text=f'- Caso clique em um local com bomba, você perde.').pack(
            padx=8, pady=8, anchor="center"))
    
    facil.assert_called

def testar_se_a_tela_de_tutorial_informa_como_se_perde_o_intermediario():
    tf = TelaDoJogo(10,16,30,tela)

    intermediario = Mock(spec=Label(Toplevel(tf.root), text=f'- Caso clique em um local com bomba, você perde.').pack(
            padx=8, pady=8, anchor="center"))
    
    intermediario.assert_called

def testar_se_a_tela_de_tutorial_informa_como_se_perde_o_jogo_dificil():
    td = TelaDoJogo(8,8,10,tela)

    dificil = Mock(spec=Label(Toplevel(td.root), text=f'- Caso clique em um local com bomba, você perde.').pack(
            padx=8, pady=8, anchor="center"))
    
    dificil.assert_called

def testar_se_a_tela_de_tutorial_informa_a_quatidade_de_bandeiras_facil():
    tf = TelaDoJogo(8,8,10,tela)

    facil = Mock(Label(Toplevel(tf.root), text=f'- Você tem um total de {tf.bombas} bandeiras.').pack(
            padx=8, pady=8, anchor="center"))
    
    facil.assert_called

def testar_se_a_tela_de_tutorial_informa_a_quatidade_de_bandeiras_intermediario():
    ti = TelaDoJogo(10,16,30,tela)

    intermediario = Mock(Label(Toplevel(ti.root), text=f'- Você tem um total de {ti.bombas} bandeiras.').pack(
            padx=8, pady=8, anchor="center"))
    
    intermediario.assert_called

def testar_se_a_tela_de_tutorial_informa_a_quatidade_de_bandeiras_dificil():
    td = TelaDoJogo(24,24,100,tela)

    dificil = Mock(Label(Toplevel(td.root), text=f'- Você tem um total de {td.bombas} bandeiras.').pack(
            padx=8, pady=8, anchor="center"))
    
    dificil.assert_called
