from tkinter import Tk
import pytest

from views.tela_do_jogo import TelaDoJogo

tela = Tk() 

# Testar se as bombas são distribuídas de forma aleatória

@pytest.mark.parametrize("matriz,linhas, colunas, esperado", [
    ([[True, False, True, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [True, False, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,
     ),  

     ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [True, False, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, True, True, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [False, False, False, False, False, False, True, True],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, False, False, False, False],
      [True, False, True, False, True, False, True, False],
      [True, False, True, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [False, False, False, False, True, False, True, False],
      [True, False, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, True, True, False, False, False],
      [False, True, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [True, False, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, True, True]], 8, 8, 10,), 
      
      ([[False, False, False, False, True, False, True, False],
      [False, False, False, False, True, False, True, False],
      [True, False, True, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, True, True, False, False, False, False],
      [False, False, False, False, False, False, True, True]], 8, 8, 10,),
      
      ([[False, False, False, False, True, False, True, False],
      [True, False, True, False, True, False, True, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [False, False, False, False, False, False, False, False],
      [True, True, False, False, False, False, False, False],
      [False, False, False, False, False, False, True, True]], 8, 8, 10,)])
def testar_distribuicao_aleatoria_facil(matriz, linhas, colunas, esperado):

    t = TelaDoJogo(8,8,10,tela)
    cont = 0
    for l in range(linhas):
        for c in range(colunas):
            if matriz[l][c] == True:
              cont += 1
    assert t.bombas == esperado and cont == esperado



@pytest.mark.parametrize("matriz,linhas, colunas, esperado", [
    ([[True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ([[False, False, False, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ([[False, False, False, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,False,False,False,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, True, True,False,False,False,False,False,False,False,False], 
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ([[False, False, False, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, False, False, False, False,True,True,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ([[False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, True, True, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 


     ([[False, False, False, False, False, False, False, False,True,False,True,False,False,False,False,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, True, True, False, False,False,True,True,False,False,False,False,False]], 10, 16, 30,
     ), 


     ([[False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, True, True, False, True,True,False,False,False,False,False,False,False]], 10, 16, 30,
     ),  

     ([[False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, False, False,False,False,True,False,True,False,True,False],
      [True, False, True, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, True, True, True, True, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ([[False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [True, False, True, False, True, False, True, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, False, False, False, False, False, False, False,True,False,True,False,True,False,True,False],
      [False, True, True, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [False, False, False, False, False, False, False, False,False,False,False,False,False,False,False,False],
      [True, True, False, False, False, False, False, False,False,False,False,False,False,False,False,False], 
      [False, False, False, False, True, True, False, False,False,False,False,False,False,False,False,False]], 10, 16, 30,
     ), 

     ])
def testar_distribuicao_aleatoria_intermediario(matriz, linhas, colunas, esperado):

    t = TelaDoJogo(10,16,30,tela)
    cont = 0
    for l in range(linhas):
        for c in range(colunas):
            if matriz[l][c] == True:
              cont += 1
    assert t.bombas == esperado and cont == esperado
