import random

def forca(palavra_secreta):
    erros = 0;
    palavra_lista = ['_'] * len(palavra_secreta)
    palavra = ''.join(palavra_lista)
    while True:
        desenhar_forca(erros, palavra_lista)
        entrada = input('Digite uma letra: ')
        if entrada in palavra_secreta:
            if entrada == palavra_secreta:
                print('Parabéns, você acertou a palavra!')
                return
            print('Pertence!')
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == entrada:
                    palavra_lista[i] = entrada
                    palavra = ''.join(palavra_lista)
        elif entrada not in palavra_secreta:
            print('Errou!')
            erros += 1
        
        if palavra == palavra_secreta:
            if erros == 5:
                print('Ufa! Por Pouco!')
            print('Parabéns, você completou a palavra!')
            return

        if erros == 6:
            desenhar_forca(erros, palavra)
            print('Você perdeu! A palavra era: ', palavra_secreta)
            return

def ler_arquivo():
    with open('forca.txt', 'r') as file:
        lines = file.readlines()
    palavra_secreta = random.choice(lines).strip()
    return palavra_secreta

def desenhar_forca(erros, palavra):
    hangman_pics = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    '''
]
    print(hangman_pics[erros])
    for _i in range(len(palavra)):
        print(palavra[_i] + ' ', end=' ')
    print()

def play_again():
    while True:
        choice = input("Gostaria de jogar novamente? (sim/nao): ")
        if choice.lower() in ['sim', 'nao']:
            return choice.lower() == 'sim'
        else:
            print("Por favor, digite 'sim' ou 'nao'.")

if __name__ == '__main__':
    while True:
        palavra_secreta = ler_arquivo()
        forca(palavra_secreta)

        if not play_again():
            print('Obrigado por jogar!')
            break