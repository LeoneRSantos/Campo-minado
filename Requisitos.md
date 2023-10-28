# Requisitos 

<Br>

## Requisitos do jogo

**1**
- [x] O nível deve começar como "vazio", isto é, com o nível a escolher. 
  - [x] Testar se o nível começa como "vazio" 
  - [x] Testar se o nível já começa selecionado no nível fácil.
  - [x] Testar se o nível já começa selecionado no nível intermediário.
  - [x] Testar se o nível já começa selecionado no nível difícil.
  - [x] Testar entradas inválidas de nível.
  - [ ] Testar entradas válidas de nível.

<Br>

**2**
- [x] Deve ser possível escolher um nível de dificuldade. 
  - [x] Testar se é possível escolher o nível fácil. 
  - [x] Testar se é possível escolher o nível intermediário. 
  - [x] Testar se é possível escolher o nível difícil. 
  - [x] Testar se tem um menu de escolha.
  
<Br>

**3**
- [x] O tabuleiro deve ser de dimensão 8x8 no nível fácil. 
  - [x] Testar se o tabuleiro de "fácil" tem dimensão 8x8.
  - [x] Testar se o tabuleiro tem, exatamente, 8 linhas.
  - [x] Testar se o tabuleiro tem mais do que 8 linhas.
  - [x] Testar se o tabuleiro tem menos do que 8 linhas.
  - [x] Testar se o tabuleiro tem, exatamente, 8 colunas.
  - [x] Testar se o tabuleiro tem mais do que 8 colunas.
  - [x] Testar se o tabuleiro tem menos do que 8 colunas.
  - [x] Testar dimensões inválidas.
  - [x] Testar se o tabuleiro está vazio no início. 
  - [x] Testar se é possível marcar no tabuleiro. 
  - [x] Testar marcações inválidas.
  - [x] Testar a distribuição de bombas no tabuleiro.

<Br>

**4**
- [x] O jogo deve ter um tabuleiro de jogo com dimensões 10x16 para intermediário  
  - [x] Testar se o jogo em “Intermediário” tem 10x16.
  - [x] Testar se o tabuleiro tem, exatamente, 10 linhas.
  - [x] Testar se o tabuleiro tem mais do que 10 linhas.
  - [x] Testar se o tabuleiro tem menos do que 10 linhas.
  - [x] Testar se o tabuleiro tem, exatamente, 16 colunas.
  - [x] Testar se o tabuleiro tem mais do que 16 colunas.
  - [x] Testar se o tabuleiro tem menos do que 16 colunas.
  - [x] Testar dimensões inválidas.
  - [x] Testar se o tabuleiro está vazio no início.
  - [ ] Testar marcações inválidas.
  - [x] Testar se é possível marcar no tabuleiro.
  - [x] Testar se a posição de jogada está dentro do tabuleiro

<Br>

**5**
- [x] O jogo deve ter um tabuleiro de jogo com dimensões 24x24 para difícil.
  - [x] Testar se o jogo em “Difícil” tem 24x24.
  - [x] Testar dimensões inválidas.
  - [x] Testar se o tabuleiro está vazio no início
  - [x] Testar se é possível marcar no tabuleiro.
  - [ ] Testar marcações inválidas.
  - [x] Testar se a posição de jogada está dentro do tabuleiro 

<Br>

**6**
- [x] O número de bombas no tabuleiro deve ser fixo 10 bombas para fácil.
  - [x] Testar se o número de bombas do tabuleiro é maior que 10 
  - [x] Testar se o número de bombas do tabuleiro é menor que 10 
  - [ ] Testar se o tabuleiro tem, exatamente, 10 bombas.
  - [x] Testar se o tabuleiro só contém bombas 
  - [x] Testar se o tabuleiro não contém bombas
  - [x] Testar se as bombas estão posicionadas em locais válidos
  - [x] Testar se existe alguma bomba no tabuleiro
  - [x] Testar se o número de bombas é negativo
  - [x] Testar se as bombas são válidas (precisa ser True)
  - [x] Testar se existem espaços suficientes para as bombas
  - [x] Testar se o tabuleiro é de tamanho vazio


<Br>

**7**
- [x] O número de bombas no tabuleiro deve ser fixo 30 bombas para intermediário.
  - [x] Testar se o número de bombas do tabuleiro é maior que 30
  - [x] Testar se o número de bombas do tabuleiro é menor que 30
  - [ ] Testar se o tabuleiro tem, exatamente, 30 bombas.
  - [x] Testar se o tabuleiro só contém bombas 
  - [x] Testar se o tabuleiro não contém bombas
  - [x] Testar se as bombas estão posicionadas em locais válidos
  - [x] Testar se existe alguma bomba no tabuleiro
  - [x] Testar se o número de bombas é negativo
  - [x] Testar se as bombas são válidas (precisa ser True)
  - [x] Testar se existem espaços suficientes para as bombas
  - [x] Testar se o tabuleiro é de tamanho vazio

<Br>

**8**
- [x] O número de bombas no tabuleiro deve ser fixo 100 bombas para difícil.
  - [x] Testar se o número de bombas do tabuleiro é maior que 100
  - [x] Testar se o número de bombas do tabuleiro é menor que 100
  - [ ] Testar se o tabuleiro tem, exatamente, 100 bombas.
  - [x] Testar se o tabuleiro só contém bombas 
  - [x] Testar se o tabuleiro não contém bombas
  - [x] Testar se as bombas estão posicionadas em locais válidos
  - [x] Testar se existe alguma bomba no tabuleiro
  - [x] Testar se o número de bombas é negativo
  - [x] Testar se as bombas são válidas (precisa ser True)
  - [x] Testar se existem espaços suficientes para as bombas
  - [x] Testar se o tabuleiro é de tamanho vazio

<Br>

**9**
- [x] O tabuleiro deve ser gerado aleatoriamente a cada partida, garantindo que as bombas estejam distribuídas de forma aleatória. 
  - [x] Testar se o tabuleiro é gerado no nível fácil;
  - [x] Testar se o tabuleiro é gerado no nível intermediário;
  - [x] Testar se o tabuleiro é gerado no nível difícil;
  - [x] Testar se as bombas são distribuídas de forma aleatória no nível fácil;
  - [x] Testar se as bombas são distribuídas de forma aleatória no nível intermediário;
  - [x] Testar se as bombas são distribuídas de forma aleatória no nível difícil;

<Br>

**10**
- [x] Todas as zonas do tabuleiro devem começar cobertas e sem bandeira. 
  - [x] Verificar se as zonas estão todas cobertas no nível fácil.
  - [x] Verificar se as zonas estão todas cobertas no nível intermediário.
  - [x] Verificar se as zonas estão todas cobertas no nível difícil.
  - [x] Verificar se nenhuma zona tem bandeira no nível fácil
  - [x] Verificar se nenhuma zona tem bandeira no nível intermediário;
  - [x] Verificar se nenhuma zona tem bandeira no nível difícil.

<Br>

**11**
- [x] O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
  - [x] Testar se é possível adicionar uma bandeira no nível fácil;
  - [x] Testar se é possível adicionar uma bandeira no nível intermediário;
  - [x] Testar se é possível adicionar uma bandeira no nível difícil;
  - [x] Testar se a zona está coberta no nível fácil;
  - [x] Testar se a zona está coberta no nível intermediário;
  - [x] Testar se a zona está coberta no nível difícil;
  - [x] Testar se a zona está descoberta no nível fácil;
  - [x] Testar se a zona está descoberta no nível intermediário;
  - [x] Testar se a zona está descoberta no nível difícil;
  - [x] Testar se a posição clicada está dentro do tabuleiro no nível fácil;
  - [x] Testar se a posição clicada está dentro do tabuleiro no nível intermediário;
  - [x] Testar se a posição clicada está dentro do tabuleiro no nível difícil;


<Br>

**12**
- [x] O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona.
  - [x] Testar se a zona que ele clicou é uma zona com bandeira no nível fácil;
  - [x] Testar se a zona que ele clicou é uma zona com bandeira no nível intermediário;
  - [x] Testar se a zona que ele clicou é uma zona com bandeira no nível difícil;
  - [x] Testar se a zona que ele clicou é uma zona descoberta no nível fácil
  - [x] Testar se a zona que ele clicou é uma zona descoberta no nível intermediário;
  - [x] Testar se a zona que ele clicou é uma zona descoberta no nível difícil
  - [x] Testar se a zona que ele clicou é uma zona coberta no nível fácil.
  - [x] Testar se a zona que ele clicou é uma zona coberta no nível intermediário.
  - [x] Testar se a zona que ele clicou é uma zona coberta no nível difícil.
  - [x] Testar se a zona foi marcada com bandeira após o click no nível fácil;
  - [x] Testar se a zona foi marcada com bandeira após o click no nível intermediário;
  - [x] Testar se a zona foi marcada com bandeira após o click no nível difícil;

<Br>

**13**
- [x] O jogador deve ser capaz de descobrir uma zona que não tenha uma bandeira.
  - [x] Testar se a zona que ele clicou tem bandeira no nível fácil
  - [x] Testar se a zona que ele clicou tem bandeira no nível intermediário
  - [x] Testar se a zona que ele clicou tem bandeira no nível difícil.
  - [x] Testar se a zona que ele clicou já está descoberta no nível fácil.
  - [x] Testar se a zona que ele clicou já está descoberta no nível intermediário.
  - [x] Testar se a zona que ele clicou já está descoberta no nível difícil.
  - [x] Testar se a zona que ele clicou está coberta no nível fácil.
  - [x] Testar se a zona que ele clicou está coberta no nível intermediário.
  - [x] Testar se a zona que ele clicou está coberta no nível difícil.
  - [x] Testar se a zona que ele clicou contém bomba
  - [x] testar se a zona foi descoberta após o click

<Br>

**14**
- [x] Não deve ser possível descobrir uma zona que tenha uma bandeira. O jogador deve ser notificado se tentar fazê-lo. 
  - [x] Testar se o jogador é informado em caso de descobrir uma zona que tenha bandeira
  - [x] Testar se ao tentar descobrir uma zona com bandeira, o tabuleiro permanece inalterado

<Br>

**15**
- [x] Não deve ser possível colocar uma bandeira em uma zona que já foi descoberta.
  - [x] Testar se é possível adicionar bandeira em local descoberto no fácil.
  - [x] Testar se é possível adicionar bandeira em local descoberto no intermediário.
  - [x] Testar se é possível adicionar bandeira em local descoberto no difícil.
  - [x] Testar se o botão é desativado quando a casa é descoberta no facil.
  - [x] Testar se o botão é desativado quando a casa é descoberta no intermediário.
  - [x] Testar se o botão é desativado quando a casa é descoberta no difícil.

<Br>

**16**
- [x] O jogo deve revelar o número de bombas adjacentes a uma zona quando ela for descoberta.
  - [x] Testar se a zona clicada contém bomba no nível fácil.
  - [x] Testar se a zona clicada contém bomba no nível intermediário.
  - [x] Testar se a zona clicada contém bomba no nível difícil.
  - [x] Testar se o cálculo de adjacência está correto no nível fácil.
  - [x] Testar se o cálculo de adjacência está correto no nível intermediário.
  - [x] Testar se o cálculo de adjacência está correto no nível difícil.


<Br>

**17**
- [x] O software deve exibir o número de bandeiras disponíveis para uso.
  - [x] Testar se o número de bandeiras está correto para o nível fácil;
  - [x] Testar se o número de bandeiras está correto para o nível intermediário; 
  - [x] Testar se o número de bandeiras está correto para o nível difícil; 

<Br>

**18**
- [x] O software deve mostrar todas as casas que continham bombas ao clicar em uma.
  - [x] Testar se existe alguma casa com bomba coberta no nível fácil.
  - [x] Testar se existe alguma casa com bomba coberta no nível intermediário.
  - [x] Testar se existe alguma casa com bomba coberta no nível difícil.

<Br>

**19**
- [x] O software deve fornecer uma mensagem de derrota quando uma área com bomba for descoberta.
  - [x] Testar se o jogador clicou em uma bomba no nível fácil.
  - [x] Testar se o jogador clicou em uma bomba no nível intermediario.
  - [x] Testar se o jogador clicou em uma bomba no nível difícil.
  - [x] Testar se a mensagem foi exibida no nível fácil.
  - [x] Testar se a mensagem foi exibida no nível intermediário.
  - [x] Testar se a mensagem foi exibida no nível difícil.

<Br>

**20**
- [x] O jogo deve continuar até que uma bomba seja encontrada.
  - [x] Testar se o jogo para ao encontrar uma bomba no nível fácil.
  - [x] Testar se o jogo para ao encontrar uma bomba no nível intermediário.
  - [x] Testar se o jogo para ao encontrar uma bomba no nível difícil.

<Br>

**21**
- [x] O jogador deve ser informado sobre o número de bombas no tabuleiro antes de iniciar o jogo.
  - [x] Testar se o número de bombas está adequado para o nível fácil;
  - [x] Testar se o número de bombas está adequado para o nível intermediário;
  - [x] Testar se o número de bombas está adequado para o nível difícil;
  - [x] Testar se o o jogador é informado da quantidade de bombas antes de começar o jogo no nível fácil. 
  - [x] Testar se o o jogador é informado da quantidade de bombas antes de começar o jogo no nível intermediário.
  - [x] Testar se o o jogador é informado da quantidade de bombas antes de começar o jogo no nível defícil.

<Br>

**22**
- [x] O Jogo deve continuar quando um local sem bomba é clicado.
  - [x] Testar se o jogo continua quando um local sem bomba é clicado no nível fácil. 
  - [x] Testar se o jogo continua quando um local sem bomba é clicado no nível intermediário.
  - [x] Testar se o jogo continua quando um local sem bomba é clicado no nível difícil.
  - [x] Testar se o jogo para quando um local com bomba é clicado o nível fácil.
  - [x] Testar se o jogo para quando um local com bomba é clicado o nível intermediário.
  - [x] Testar se o jogo para quando um local com bomba é clicado o nível difícil.

<Br>

**23**
- [x] O jogo não deve ser afetado quando uma bandeira é adicionada.
  - [x] Testar se o jogo continua ao ser adicionada uma bandeira no nível fácil.
  - [x] Testar se o jogo continua ao ser adicionada uma bandeira no nível intermediário.
  - [x] Testar se o jogo continua ao ser adicionada uma bandeira no nível difícil.
  - [x] Testar se o jogo para quando uma bandeira é adicionada no nível fácil.
  - [x] Testar se o jogo para quando uma bandeira é adicionada no nível intermediário.
  - [x] Testar se o jogo para quando uma bandeira é adicionada no nível difícil.

<Br>

## Requisitos da interface

**24**
- [ ] Deve ser possível começar com uma tela de escolha de nível de dificuldade.
  - [ ] Testar se a tela mostra todos os níveis que se pode escolher.
  - [ ] Testar se a tela de escolha de nível de dificuldade é criada.
  - [ ] Testar se é possível escolher o nível fácil a partir da tela.
  - [ ] Testar se é possível escolher o nível intermediário a partir da tela.
  - [ ] Testar se é possível escolher o nível difícil a partir da tela.

**25**
- [ ] Após a escolha do nível fácil, deve-se gerar a tela do tabuleiro fácil.
  - [ ] Testar se a tela do tabuleiro fácil é gerada.
  - [ ] Testar se ela tem a proporção de 8x8 casas.
  - [ ] Testar se o tabuleiro inicia vazio.
  - [ ] Testar se é possível marcar dentro do tabuleiro. 
  - [ ] Testar se é possível descobrir uma bomba ou o número de bombas adjacentes ao se descobrir uma casa do tabuleiro.
  - [ ] Testar se é possível adicionar uma bandeira em uma casa.
  - [ ] Testar se é possível remover uma bandeira de uma casa.
  - [ ] Testar se a casa fica desativada ao ser descoberta e encontrar um número que indique adjacência de bombas.
  - [ ] Testar se todas as casas do tabuleiro ficam desativadas após encontrar uma boba.
  - [ ] Testar se todas as bombas do tabuleiro são mostradas ao se descobrir uma bomba.

**26**
- [ ] Após a escolha do nível intermediário, deve-se gerar a tela do tabuleiro intermediário.
  - [ ] Testar se a tela do tabuleiro intermediário é gerada.
  - [ ] Testar se ela tem a proporção de 10x16 casas.
  - [ ] Testar se o tabuleiro inicia vazio.
  - [ ] Testar se é possível marcar dentro do tabuleiro. 
  - [ ] Testar se é possível descobrir uma bomba ou o número de bombas adjacentes ao se descobrir uma casa do tabuleiro.
  - [ ] Testar se é possível adicionar uma bandeira em uma casa.
  - [ ] Testar se é possível remover uma bandeira de uma casa.
  - [ ] Testar se a casa fica desativada ao ser descoberta e encontrar um número que indique adjacência de bombas.
  - [ ] Testar se todas as casas do tabuleiro ficam desativadas após encontrar uma boba.
  - [ ] Testar se todas as bombas do tabuleiro são mostradas ao se descobrir uma bomba.

**27**
- [ ] Após a escolha do nível difícil, deve-se gerar a tela do tabuleiro difícil.
  - [ ] Testar se a tela do tabuleiro difícil é gerada.
  - [ ] Testar se ela tem a proporção de 24x24 casas.
  - [ ] Testar se o tabuleiro inicia vazio.
  - [ ] Testar se é possível marcar dentro do tabuleiro. 
  - [ ] Testar se é possível descobrir uma bomba ou o número de bombas adjacentes ao se descobrir uma casa do tabuleiro.
  - [ ] Testar se é possível adicionar uma bandeira em uma casa.
  - [ ] Testar se é possível remover uma bandeira de uma casa.
  - [ ] Testar se a casa fica desativada ao ser descoberta e encontrar um número que indique adjacência de bombas.
  - [ ] Testar se todas as casas do tabuleiro ficam desativadas após encontrar uma boba.
  - [ ] Testar se todas as bombas do tabuleiro são mostradas ao se descobrir uma bomba.

**28**
- [ ] Após escolher o nível de dificuldade, deve-se gerar, tamém, uma tela de tutorial que mostra informações sobre o nível escolhido e como jogar.
  - [ ] Testar se a tela de tutorial é gerada.
  - [ ] Testar se a tela de tutorial informa o nível escolhido.
  - [ ] Testar se a tela de tutorial informa as proporções do tabuleiro.
  - [ ] Testar se a tela de tutorial informa a quantidade de bombas daquele nível.
  - [ ] Testar se a tela de tutorial informa a quantidade de bandeiras daquele nível.
  - [ ] Testar se a tela de tutorial informa como vencer o jogo.
  - [ ] Testar se a tela de tutorial informa como se perde o jogo.

**29**
- [ ] Após a geração do tabuleiro no nível fácil, o clique em cada uma das casas deve revelar a casa.
  - [ ] Testar se é possível verificar uma casa através do clique.
  - [ ] Testar se a casa revela um número que indica adjecência.
  - [ ] Testar se a casa revela uma bomba.
  - [ ] Testar se a casa, após revelada, ainda pode ser verificada.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada.

**30**
- [ ] Após a geração do tabuleiro no nível intermediário, o clique em cada uma das casas deve revelar a casa.
  - [ ] Testar se é possível verificar uma casa através do clique.
  - [ ] Testar se a casa revela um número que indica adjecência.
  - [ ] Testar se a casa revela uma bomba.
  - [ ] Testar se a casa, após revelada, ainda pode ser verificada.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada.

**31**
- [ ] Após a geração do tabuleiro no nível difícil, o clique em cada uma das casas deve revelar a casa.
  - [ ] Testar se é possível verificar uma casa através do clique.
  - [ ] Testar se a casa revela um número que indica adjecência.
  - [ ] Testar se a casa revela uma bomba.
  - [ ] Testar se a casa, após revelada, ainda pode ser verificada.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada.

**32**
- [ ] Caso a casa verificada no tabuleiro fácil conter uma bomba, todas as casas que contém bombas devem ser reveladas.
  - [ ] Testar se é possível verificar uma casa que contém bomba.
  - [ ] Testar se, após encontrar uma bomba, as demais casas com bombas são mostradas.
  - [ ] Testar se as demais casas já verificadas que não contém bombas não sofrem alteração.
  - [ ] Testar se as casas com bombas são reveladas com destaque suficiente.

**33**
- [ ] Caso a casa verificada no tabuleiro intermediário conter uma bomba, todas as casas que contém bombas devem ser reveladas.
  - [ ] Testar se é possível verificar uma casa que contém bomba.
  - [ ] Testar se, após encontrar uma bomba, as demais casas com bombas são mostradas.
  - [ ] Testar se as demais casas já verificadas que não contém bombas não sofrem alteração.
  - [ ] Testar se as casas com bombas são reveladas com destaque suficiente.

**34**
- [ ] Caso a casa verificada no tabuleiro difícil conter uma bomba, todas as casas que contém bombas devem ser reveladas.
  - [ ] Testar se é possível verificar uma casa que contém bomba.
  - [ ] Testar se, após encontrar uma bomba, as demais casas com bombas são mostradas.
  - [ ] Testar se as demais casas já verificadas que não contém bombas não sofrem alteração.
  - [ ] Testar se as casas com bombas são reveladas com destaque suficiente.

**35** 
- [ ] Caso a casa verificada no nível fácil conter uma bomba, uma mensagem de derrota deve ser exibida.
  - [ ] Testar se a mensagem de derrota é criada.
  - [ ] Verificar se ela informa que o jogador perdeu por encontrar uma bomba.
  - [ ] Testar se ela se sobrepõe a tela anterior.
  - [ ] Testar se ela é criada separadamente.
  - [ ] Testar se, ao criar a nova tela, a tela anterior é interrompida.
  - [ ] Testar se ao fechar a tela de mensagem de derrota, a tela do tabuleiro também é fechada.

**36** 
- [ ] Caso a casa verificada no nível intermediário conter uma bomba, uma mensagem de derrota deve ser exibida.
  - [ ] Testar se a mensagem de derrota é criada.
  - [ ] Verificar se ela informa que o jogador perdeu por encontrar uma bomba.
  - [ ] Testar se ela se sobrepõe a tela anterior.
  - [ ] Testar se ela é criada separadamente.
  - [ ] Testar se, ao criar a nova tela, a tela anterior é interrompida.
  - [ ] Testar se ao fechar a tela de mensagem de derrota, a tela do tabuleiro também é fechada.

**37** 
- [ ] Caso a casa verificada no nível difícil conter uma bomba, uma mensagem de derrota deve ser exibida.
  - [ ] Testar se a mensagem de derrota é criada.
  - [ ] Verificar se ela informa que o jogador perdeu por encontrar uma bomba.
  - [ ] Testar se ela se sobrepõe a tela anterior.
  - [ ] Testar se ela é criada separadamente.
  - [ ] Testar se, ao criar a nova tela, a tela anterior é interrompida.
  - [ ] Testar se ao fechar a tela de mensagem de derrota, a tela do tabuleiro também é fechada.

**38**
- [ ] Em situação de derrota no nível fácil, o tabuleiro deve ser desativado e apenas revelar as casa que contém bombas.
  - [ ] Testar se o tabuleiro é desativado após encontrar uma bomba.
  - [ ] Testar se as demais casas já verificadas permanecem como estão.
  - [ ] Testar se novas casas que não contém bombas são reveladas.

**39**
- [ ] Em situação de derrota no nível intermediário, o tabuleiro deve ser desativado e apenas revelar as casa que contém bombas.
  - [ ] Testar se o tabuleiro é desativado após encontrar uma bomba.
  - [ ] Testar se as demais casas já verificadas permanecem como estão.
  - [ ] Testar se novas casas que não contém bombas são reveladas.

**40**
- [ ] Em situação de derrota no nível difícil, o tabuleiro deve ser desativado e apenas revelar as casa que contém bombas.
  - [ ] Testar se o tabuleiro é desativado após encontrar uma bomba.
  - [ ] Testar se as demais casas já verificadas permanecem como estão.
  - [ ] Testar se novas casas que não contém bombas são reveladas.

**41**
- [ ] Deve ser possível adicionar uma bandeira nas casas em que o jogador supõe conter bomba no nível fácil.
  - [ ] Testar se é possível adicionar uma bandeira em qualquer casa.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada com adjacência.
  - [ ] Testar se é possível adicionar uma bandeira numa casa que foi revelada contendo bomba.

**42**
- [ ] Deve ser possível adicionar uma bandeira nas casas em que o jogador supõe conter bomba no nível intermediário.
  - [ ] Testar se é possível adicionar uma bandeira em qualquer casa.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada com adjacência.
  - [ ] Testar se é possível adicionar uma bandeira numa casa que foi revelada contendo bomba.

**43**
- [ ] Deve ser possível adicionar uma bandeira nas casas em que o jogador supõe conter bomba no nível difícil.
  - [ ] Testar se é possível adicionar uma bandeira em qualquer casa.
  - [ ] Testar se é possível adicionar uma bandeira numa casa já verificada com adjacência.
  - [ ] Testar se é possível adicionar uma bandeira numa casa que foi revelada contendo bomba.
