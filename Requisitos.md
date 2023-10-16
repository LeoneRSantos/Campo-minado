# Requisitos 

**1**
- [x] O nível deve começar como "vazio", isto é, com o nível a escolher. 
  - Testar se o nível começa como "vazio" 

**2**
- [x] Deve ser possível escolher um nível de dificuldade. 
  - Testar se é possível escolher o nível fácil. 
  - Testar se é possível escolher o nível intermediário. 
  - Testar se é possível escolher o nível difícil. 
  - Testar se tem um menu de escolha.
  - 
**3**
- [x] O tabuleiro deve ser de dimensão 8x8 no nível fácil. 
  - Testar se o tabuleiro de "fácil" tem dimensão 8x8. 
  - Testar se o tabuleiro está vazio no início. 
  - Testar se é possível marcar no tabuleiro. 
  - Testar se a marcação do tabueiro está dentro dele. 
  - Testar a distribuição de bombas no tabuleiro.

**4**
- [x] O jogo deve ter um tabuleiro de jogo com dimensões 10x16 para intermediário  
  - Testar se o jogo em “Intermediário” tem 10x16
  - Testar se o tabuleiro está vazio no início
  - Testar se é possível marcar no tabuleiro
  - Testar se a posição de jogada está dentro do tabuleiro

**5** 
- [x] O jogo deve ter um tabuleiro de jogo com dimensões 24x24 para difícil.
  - Testar se o jogo em “Difícil” tem 24x24
  - Testar se o tabuleiro está vazio no início
  - Testar se é possível marcar no tabuleiro
  - Testar se a posição de jogada está dentro do tabuleiro 

**6**
- [x] O número de bombas no tabuleiro deve ser fixo 10 bombas para fácil.
  - verificar se o número de bombas do tabuleiro é maior que 10 [x]
  - verificar se o número de bombas do tabuleiro é menor que 10 [x]
  - verificar se o tabuleiro só contém bombas [x]
  - verificar se o tabuleiro não contém bombas[x]
  - Testar se as bombas estão posicionadas em locais válidos[x]
  - Testar se existe alguma bomba no tabuleiro[x]
  - Testar se o número de bombas é negativo[x]
  - Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar)[x]
  - Testar se existem espaços suficientes para as bombas[x]
  - Testar se o tabuleiro é de tamanho vazio[x]


**7**
- [x] O número de bombas no tabuleiro deve ser fixo 30 bombas para intermediário.
  - verificar se o número de bombas do tabuleiro é maior que 30[x]
  - verificar se o número de bombas do tabuleiro é menor que 30[x]
  - verificar se o tabuleiro só contém bombas [x]
  - verificar se o tabuleiro não contém bombas[x]
  - Testar se as bombas estão posicionadas em locais válidos[x]
  - Testar se existe alguma bomba no tabuleiro[x]
  - Testar se o número de bombas é negativo[x]
  - Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar)[x]
  - Testar se existem espaços suficientes para as bombas[x]
  - Testar se o tabuleiro é de tamanho vazio[x]

**8**
- [x] O número de bombas no tabuleiro deve ser fixo 100 bombas para difícil.
  - verificar se o número de bombas do tabuleiro é maior que 100[x]
  - verificar se o número de bombas do tabuleiro é menor que 100[x]
  - verificar se o tabuleiro só contém bombas [x]
  - verificar se o tabuleiro não contém bombas[x]
  - Testar se as bombas estão posicionadas em locais válidos[x]
  - Testar se existe alguma bomba no tabuleiro[x]
  - Testar se o número de bombas é negativo[x]
  - Testar se as bombas são válidas (ex: no código precisa ser inteiro, passamos uma string para testar)[x]
  - Testar se existem espaços suficientes para as bombas[x]
  - Testar se o tabuleiro é de tamanho vazio[x]

**9**
- [x] O tabuleiro deve ser gerado aleatoriamente a cada partida, garantindo que as bombas estejam distribuídas de forma aleatória. 
  - [x] Testar se o tabuleiro é gerado
  - [x] Testar se as bombas são distribuídas de forma aleatória 

**10**
- [] Todas as zonas do tabuleiro devem começar cobertas e sem bandeira. 
  - Verificar se as zonas estão todas cobertas
  - Verificar se nenhuma zona tem bandeira 

**11**
- [] O jogador deve ser capaz de marcar uma zona com uma bandeira para indicar que ele considera ter uma bomba.
  - Testar se é possível adicionar uma bandeira
  - Testar se a zona está coberta
  - Testar se a zona está descoberta
  - Testar se a posição clicada está dentro do tabuleiro


**12**
- [] O jogador deve ser capaz de remover uma bandeira previamente colocada em uma zona.
  - verificar se a zona que ele clicou é uma zona com bandeira
  - verificar se a zona que ele clicou é uma zona descoberta
  - verificar se a zona que ele clicou é uma zona coberta.
  - Testar se a zona foi marcada com bandeira após o click

**13**
- [] O jogador deve ser capaz de descobrir uma zona que não tenha uma bandeira.
  - verificar se a zona que ele clicou tem bandeira
  - verificar se a zona que ele clicou já está descoberta
  - verificar se a zona que ele clicou está coberta.
  - verificar se a zona que ele clicou contém bomba
  - testar se a zona foi descoberta após o click

**14**
- [] Não deve ser possível descobrir uma zona que tenha uma bandeira. O jogador deve ser notificado se tentar fazê-lo. 
  - Testar se o jogador é informado em caso de descobrir uma zona que tenha bandeira
  - Testar se ao tentar descobrir uma zona com bandeira, o tabuleiro permanece inalterado

**15**
- [] Não deve ser possível colocar uma bandeira em uma zona que já foi descoberta. O jogador deve ser notificado se tentar fazê-lo.
  - Testar se o jogador é informado que a zona selecionada já está descoberta

**16** 
- [] O jogo deve revelar o número de bombas adjacentes a uma zona quando ela for descoberta.
  - verificar se a zona clicada contém bomba
  - verificar se o cálculo de adjacência está correto

**17**
- [] O software deve mostrar o tempo decorrido durante a partida. 
  - Testar se o cronômetro se inicia ao iniciar o jogo.

**18**
- [] O software deve exibir o número de bandeiras disponíveis para uso.
  - Testar se o número de bandeiras está correto para o nível fácil;
  - Testar se o número de bandeiras está correto para o nível intermediário; 
  - Testar se o número de bandeiras está correto para o nível difícil; 

**19**
- [] O software deve fornecer uma mensagem de vitória quando todas as áreas sem bombas forem descobertas corretamente.
  - verificar se existe alguma bomba descoberta
  - verificar se existe alguma zona sem bomba coberta
  - verificar se a mensagem de vitória está sendo exibida corretamente
  - verificar se o usuário retorna ao menu inicial após a mensagem de vitória

**20**
- [] O software deve fornecer uma mensagem de derrota quando uma área com bomba for descoberta.
  - verificar se o jogador clicou em uma bomba.
  - Verificar se a mensagem foi exibida.

**21**
- [] O software deve verificar se todas as áreas sem bombas foram descobertas corretamente para determinar a vitória.
  - Testar se todas as áreas com bomba foram descobertas.

**22**
- [] O jogador deve ser informado sobre o número de bombas no tabuleiro antes de iniciar o jogo.
  - Testar se o número de bombas está adequado para o nível fácil;
  - Testar se o número de bombas está adequado para o nível intermediário;
  - Testar se o número de bombas está adequado para o nível difícil;
  - Testar se o o jogador é informado da quantidade de bombas antes de começar o jogo.

**23**
- [] O Jogo deve continuar quando um local sem bomba é clicado.
  - Verificar se o jogo continua quando um local sem bomba é clicado.
  - Verificar se o jogo para quando um local com bomba é clicado.

**24**
- [] O jogo não deve ser afetado quando uma bandeira é adicionada.
  - Testar se o jogo continua ao ser adicionada uma bandeira.
  - Testar se o jogo para quando uma bandeira é adicionada.

**25**
- [] Quando o jogo parar, o cronômetro deve ser pausado.
  - Testar se o cronômetro é pausado quando o jogo é encerrado. 
  - Testar se o cronômetro continua quando o jogo é encerrado.
