from tkinter import Tk
import pytest

from views.tela_do_jogo import TelaDoJogo


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
def testarCalcularNumeroDeBombasFacil(matriz, linhas, colunas, esperado):
    t = Tk()
    t = TelaDoJogo(8,8,10,t)
    cont = 0
    for l in range(linhas):
        for c in range(colunas):
            if matriz[l][c] == True:
              cont += 1
    assert t.bombas == esperado and cont == esperado
