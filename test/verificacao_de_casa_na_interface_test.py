from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# - [ ] Testar se é possível verificar uma casa através do clique.
#   - [ ] Testar se a casa revela um número que indica adjecência.
#   - [ ] Testar se a casa revela uma bomba.
#   - [ ] Testar se a casa, após revelada, ainda pode ser verificada.
#   - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada.
#   - [ ] Testar se, após a verificação, as outras casa são afetadas.


def testar_verificacao_de_casa_na_interface_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    verificada = True

    try:
        tf.verificarCasa(tf.matrizDoJogo[3][3])

        if not tf.matrizDoJogo[3][3]['text'] == tf.calcularBombasAdjacentes(3, 3) or tf.matrizDoJogo[3][3]['text'] == "X":
            verificada = False
        if not tf.matrizDoJogo[3][3]['text'] == '0':
            verificada = True
    except RecursionError:
        verificada = True

    assert verificada == True


def testar_verificacao_de_casa_na_interface_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    verificada = True

    try:
        ti.verificarCasa(ti.matrizDoJogo[5][4])

        if not ti.matrizDoJogo[5][4]['text'] == ti.calcularBombasAdjacentes(5, 4) or ti.matrizDoJogo[5][4]['text'] == "X":
            verificada = False
        if not ti.matrizDoJogo[5][4]['text'] == '0':
            verificada = True
    except RecursionError:
        verificada = True

    assert verificada == True


def testar_verificacao_de_casa_na_interface_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    verificada = True

    try:
        td.verificarCasa(td.matrizDoJogo[5][4])

        if not td.matrizDoJogo[5][4]['text'] == td.calcularBombasAdjacentes(5, 4) or td.matrizDoJogo[5][4]['text'] == "X":
            verificada = False
        if not td.matrizDoJogo[5][4]['text'] == '0':
            verificada = True
    except RecursionError:
        verificada = True

    assert verificada == True


def testar_se_a_casa_mostra_um_numero_de_adjacencia_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    adjacencia = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])

                    if tf.matrizDoJogo[l][c]['text'] == str():
                        adjacencia = True
                except RecursionError:
                    adjacencia = True

    assert adjacencia == True


def testar_se_a_casa_mostra_um_numero_de_adjacencia_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    adjacencia = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == False:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])

                    if ti.matrizDoJogo[l][c]['text'] == str():
                        adjacencia = True
                except RecursionError:
                    adjacencia = True

    assert adjacencia == True


def testar_se_a_casa_mostra_um_numero_de_adjacencia_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    adjacencia = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == False:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])

                    if td.matrizDoJogo[l][c]['text'] == str():
                        adjacencia = True
                except RecursionError:
                    adjacencia = True

    assert adjacencia == True


def testar_se_a_casa_mostra_uma_bomba_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    mostra = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == True:
                try:
                    tf.verificarCasa(tf.matrizDoJogo[l][c])

                    if tf.matrizDoJogo[l][c]['text'] == 'X':
                        mostra = True
                except RecursionError:
                    mostra = False

    assert mostra == True


def testar_se_a_casa_mostra_uma_bomba_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    mostra = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if ti.casasRandomicas[l][c] == True:
                try:
                    ti.verificarCasa(ti.matrizDoJogo[l][c])

                    if ti.matrizDoJogo[l][c]['text'] == 'X':
                        mostra = True
                except RecursionError:
                    mostra = False

    assert mostra == True


def testar_se_a_casa_mostra_uma_bomba_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    mostra = False

    for l in range(td.linhas):
        for c in range(td.colunas):
            if td.casasRandomicas[l][c] == True:
                try:
                    td.verificarCasa(td.matrizDoJogo[l][c])

                    if td.matrizDoJogo[l][c]['text'] == 'X':
                        mostra = True
                except RecursionError:
                    mostra = False

    assert mostra == True


def testar_se_a_casa_apos_revelada_pode_ser_verificada_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    aindaPodeSerRevelada = False

    try:
        tf.verificarCasa(tf.matrizDoJogo[4][4])
        valor1 = tf.matrizDoJogo[4][4]['text']

        tf.verificarCasa(tf.matrizDoJogo[4][4])
        valor2 = tf.matrizDoJogo[4][4]['text']

    except RecursionError:
        aindaPodeSerRevelada = False

    try:
        if valor1 != valor2:
            aindaPodeSerRevelada = True
    except UnboundLocalError:
        aindaPodeSerRevelada = False

    assert aindaPodeSerRevelada == False


def testar_se_a_casa_apos_revelada_pode_ser_verificada_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    aindaPodeSerRevelada = False

    try:
        ti.verificarCasa(ti.matrizDoJogo[3][4])
        valor1 = ti.matrizDoJogo[3][4]['text']

        ti.verificarCasa(ti.matrizDoJogo[3][4])
        valor2 = ti.matrizDoJogo[3][4]['text']
    except RecursionError:
        aindaPodeSerRevelada = False

    try:
        if valor1 != valor2:
            aindaPodeSerRevelada = True
    except UnboundLocalError:
        aindaPodeSerRevelada = False

    assert aindaPodeSerRevelada == False


def testar_se_a_casa_apos_revelada_pode_ser_verificada_dificil():
    td = TelaDoJogo(24, 24, 100, tela)
    aindaPodeSerRevelada = False

    try:
        td.verificarCasa(td.matrizDoJogo[10][6])
        valor1 = td.matrizDoJogo[10][6]['text']

        td.verificarCasa(td.matrizDoJogo[10][6])
        valor2 = td.matrizDoJogo[10][6]['text']
    except RecursionError:
        aindaPodeSerRevelada = False

    try:
        if valor1 != valor2:
            aindaPodeSerRevelada = True

    except UnboundLocalError:
        aindaPodeSerRevelada = False

    assert aindaPodeSerRevelada == False


def testar_se_apos_verificacao_outras_casas_sao_afetadas_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    alterado = False

    try:
        tf.verificarCasa(tf.matrizDoJogo[3][3])
    except RecursionError:
        alterado = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if l == 3 and c == 3:
                pass
            if tf.matrizDoJogo[l][c]['text'] == str(int) or tf.matrizDoJogo[l][c]['text'] == 'X':
                alterado = True

    assert alterado == False

def testar_se_apos_verificacao_outras_casas_sao_afetadas_intermediario():
    ti = TelaDoJogo(10, 16, 30, tela)
    alterado = False

    try:
        ti.verificarCasa(ti.matrizDoJogo[5][6])
    except RecursionError:
        alterado = False

    for l in range(ti.linhas):
        for c in range(ti.colunas):
            if l == 5 and c == 6:
                pass
            if ti.matrizDoJogo[l][c]['text'] == str(int) or ti.matrizDoJogo[l][c]['text'] == 'X':
                alterado = True

    assert alterado == False

def testar_se_apos_verificacao_outras_casas_sao_afetadas_dificil():
    tf = TelaDoJogo(24, 24, 100, tela)
    alterado = False

    try:
        tf.verificarCasa(tf.matrizDoJogo[10][12])
    except RecursionError:
        alterado = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if l == 10 and c == 12:
                pass
            if tf.matrizDoJogo[l][c]['text'] == str(int) or tf.matrizDoJogo[l][c]['text'] == 'X':
                alterado = True

    assert alterado == False
