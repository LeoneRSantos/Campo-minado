class Dificuldade:
    nivel = ''

    def __init__(self, nivel):
        self.nivel = nivel

    def escolherNivel(self):

        if self.nivel == 'fácil':
            print('Fácil')

            return self.nivel

        elif self.nivel == 'intermediário':
            print('Intermediário')
            
            return self.nivel

        elif self.nivel == 'difícil':
            print('Difícil')
            
            return self.nivel
        
        else:
            return self.nivel
