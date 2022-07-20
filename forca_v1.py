# -*- coding: utf-8 -*-

# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from time import sleep

from numpy import empty

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:



    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.ok_words = []
        self.error_words = []
    
    # Método para sair
    def sair(self):
        print('\nSaindo em 2 segundos')
        sleep(1.5)
        print('\nGood bye!')
        sleep(0.5)
        exit(0)

    # Método para adivinhar a letra
    def guess(self, letter):
        ok = False

        # Verifica se a variável está vazia ou contem espaço
        if letter == '' or letter == ' ':
            print('É necessário digitar algo para jogar!')
            sleep(2)
            return

        # Verifica se a variável é maior que o permitido
        if len(letter) > 1:
            print('É permitido apenas uma (01) letra por vez!')
            sleep(2)
            return

        if letter == '0':
            self.sair()

        if letter in self.ok_words or letter in self.error_words:
            print('Letra já utilizada no jogo!')
            sleep(2.0)
            return

        for w in self.word:
            if letter == w:
                ok = True

        if ok:
            self.ok_words.append(letter)
        else:
            self.error_words.append(letter)

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if len(self.error_words) == 6 or self.hangman_won():
            return True

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        for w in self.word:
            ok = w in self.ok_words
            if not ok:
                return False
        return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        retorno = ''
        for w in self.word:
            if w in self.ok_words:
                retorno += w
            else:
                retorno += '_'
        return retorno

    def show_erradas(self):
        print("\nLetras erradas: %s" % (len(self.error_words)))
        for w in self.error_words:
            print("%s" % w)

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.error_words)])
        print("\n%s" % self.hide_word())
        if len(self.error_words) > 0:
            self.show_erradas()
        
        return self.hangman_over()
        


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    finishGame = False

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    print("Vamos brincar de forca")

    while not finishGame:
        # Verifica o status do jogo
        if game.print_game_status():
            finishGame = True
        else:
            # Se o jogo não terminou, solicita uma nova letra
            letra = input("\nDigite uma letra para jogar ou zero(0) para sair:\n")
            game.guess(letra)

    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! \n')

    game.sair()


# Executa o programa
if __name__ == "__main__":
    main()
