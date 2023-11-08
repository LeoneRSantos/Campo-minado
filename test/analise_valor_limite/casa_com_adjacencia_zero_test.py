from tkinter import *
from views.tela_do_jogo import TelaDoJogo

tela = Tk()

# Caso a casa verificada no nível fácil conter adjacência 0, as 8 casas adjacentes a ela devem ser descobertas.
# Caso a casa verificada no nível intermediário conter adjacência 0, as 8 casas adjacentes a ela devem ser descobertas.
# Caso a casa verificada no nível difícil conter adjacência 0, as 8 casas adjacentes a ela devem ser descobertas.


def testar_se_as_oito_casas_sao_descobertas_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    oitoCasas = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    oitoCasas = True

    assert oitoCasas == True


def testar_se_menos_que_oito_casas_sao_descobertas_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    menos = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    menos.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert not len(menos) < 8


def testar_se_mais_que_oito_casas_sao_descobertas_facil():
    tf = TelaDoJogo(8, 8, 10, tela)
    mais = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    mais.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert len(mais) > 8


def testar_se_as_oito_casas_sao_descobertas_intermediario():
    tf = TelaDoJogo(10, 16, 30, tela)
    oitoCasas = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    oitoCasas = True

    assert oitoCasas == True


def testar_se_menos_que_oito_casas_sao_descobertas_intermediario():
    tf = TelaDoJogo(10, 16, 30, tela)
    menos = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    menos.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert not len(menos) < 8


def testar_se_mais_que_oito_casas_sao_descobertas_intermediario():
    tf = TelaDoJogo(10, 16, 30, tela)
    mais = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    mais.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert len(mais) > 8


def testar_se_as_oito_casas_sao_descobertas_dificil():
    tf = TelaDoJogo(24, 24, 100, tela)
    oitoCasas = False

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    oitoCasas = True

    assert oitoCasas == True


def testar_se_menos_que_oito_casas_sao_descobertas_dificil():
    tf = TelaDoJogo(24, 24, 100, tela)
    menos = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    menos.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert not len(menos) < 8


def testar_se_mais_que_oito_casas_sao_descobertas_dificil():
    tf = TelaDoJogo(24, 24, 100, tela)
    mais = []

    for l in range(tf.linhas):
        for c in range(tf.colunas):
            if tf.casasRandomicas[l][c] == False:
                numero = tf.calcularBombasAdjacentes(l, c)
                if numero == 0:
                    for ll in range(-1, 2):
                        for cc in range(-1, 2):
                            if 0 <= l + ll < tf.linhas and 0 <= c + cc < tf.colunas:
                                if tf.matrizDoJogo[l + ll][c + cc]['text'] == str(int) or tf.matrizDoJogo[l + ll][c + cc]['text'] == '':
                                    mais.append(
                                        tf.matrizDoJogo[l + ll][c + cc])

    assert len(mais) > 8
