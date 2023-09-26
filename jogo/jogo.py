class Dificuldade:
    nivel = ''

    @staticmethod
    def escolherNivel():
        Dificuldade.nivel = str(input('Escolha a dificuldade: ')) 

        if Dificuldade.nivel == 'fácil':
            print('Fácil')

            return Dificuldade.nivel

        elif Dificuldade.nivel == 'intermediário':
            print('Intermediário')
            
            return Dificuldade.nivel

        elif Dificuldade.nivel == 'difícil':
            print('Difícil')
            
            return Dificuldade.nivel
        
        else:
            return Dificuldade.nivel
