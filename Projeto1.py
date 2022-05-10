import random
lista_tentativas = []
def mostrar_score():
    if len(lista_tentativas) <= 0:
        print('Ainda não há um recorde, é sua chance de brilhar! ')
    else:
        print(f'O recorde atual é de {min(lista_tentativas)} tentativas!')
def start_jogo():
    numero_random = int(random.randint(1, 10))
    print('Ola desafiante! Bem vindo ao jogo de adivinhação!') 
    nome_jogador = input('Qual e seu nome? ')
    quer_jogar = input(f'Ola {nome_jogador}, voce gostaria de jogar? (SIM/NAO) ')
    
    tentativas = 0
    mostrar_score()
    while quer_jogar.lower() == "sim":
        try:
            adivinhar = input('Escolha um numero entre 1 e 10 ')
            if int(adivinhar) < 1 or int(adivinhar) > 10:
                raise ValueError('Por favor escolha um numero entre os valores ditos!')
            if int(adivinhar) == numero_random:
                print('Muito bem! Voce acertou!')
                tentativas += 1
                lista_tentativas.append(tentativas)
                print(f'Voce precisou de {tentativas} tentativas!')
                jogar_novamente = input('Gostaria de jogar novamente? (SIM/NAO) ') 
                tentativas = 0
                mostrar_score()
                numero_random = int(random.randint(1, 10))
                if jogar_novamente.lower == 'nao':
                    print('Tudo bem, ate a proxima! ')
                    break
            elif int(adivinhar) > numero_random:
                    print('E menor')
                    tentativas += 1
            elif int(adivinhar) < numero_random:
                    print('E maior')
                    tentativas += 1         
        except ValueError as err:
            print('Opa! Este nao e um valor valido. Tente novamente.')
            print(f'{err}') 
    else:
        print('Tudo bem, ate a proxima!')
if __name__ == '__main__':
    start_jogo()             