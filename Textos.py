import random

def texto1():
    return '\n  Olá usuario, sejá bem vindo ao revisando conhecimento matemático, o programa ainda está em desenvolvimento, então por favor não se chatei caso de algum erro no programa, nos avise caso você encontrar um error no programa, logo em seguida você será reconpensado após checarmos o erro que você nos sitou.\n Aqui escolha uma fórmula matemática para revisar os seus conhecimentos ou aprender algo novo, apos escolher uma opção aperte enter para continuar.\n'

def apresentando_formulas():
    return '1- soma e subtração'

def soma_subtracao():
    print('\n Para fazer contas de soma e subtração é muito facil, imagine duas pessoas distantes uma da outra, logo teremos 1 pessoa no lado esquerdo (<) e 1 pessoa no lado direito (>), se agente colocarmos o sinal de soma (+) entre essas duas pessoas, agente vai está juntando essas pessoas (1 + 1) e logo o que seria 1 pessoa no lado esquerdo e 1 pessoa no lado direito, teremos 2 pessoas em um lugar só.\n\n  Agora imagina 2 pessoas no lado esquerdo (<) e 1 pessoal no lado direito (>) e no meio dessas pessoas o sinal de soma (+), quando fazemos isso (2 + 1) estaremos juntando as 2 pessoas do lado esquerdo com 1 pessoa sozinha do lado direito, logo teremos 3 pessoas juntas. Vamos inverter, no lado esquerdo (<) tem 1 pessoa sozinha e no lado direito (>)tem 2 pessoas juntas, se colocarmos no meio deles o sinal de soma (+) a gente vai juntar (1 + 2), a unica pessoa no lado esquerdo com as 2 outras pessoas do lado direito, logo teremos 3 pessoas juntas.\n\n Mas para que você faça a conta mais rapido coloca o maior número no lado esquerdo e o menor numero no lado direito.\n\n Bom para fazer conta de soma você vai pegar o maior número e a partir dele você vai continuar contando mais e mais, até você ter contado vezes igual ao numero menos, exemplo 10 + 5, você vai começar do 10 e vai continuar, 11, 12, 13... até você ter continuado 5 vezes.\n')
    
    print('Vamos ver se você aprendeu, reponda essa pergunta.\n\nSe temos 3 pessoas em um lado e 2 pessoas no outro lado, e um sinal de soma (+), quantas pessoas vão ficar em um lugar só?')

    interesse= input('Você quer tentar responder a pergunta?\n[S] Sim\n[N] Não\n>> ').lower()
    if interesse == 'n':
        print('...')
    
    elif interesse == 's':
        respostas= {'Resposta_Certa': 'As 3 pessoas vão se juntar as 2 pessoas e vamos ter 5 pessoas em um lugar só.', 'Resposta_Errada': 'As 3 pessoas vão se juntar as 2 pessoas e vamos ter 6 pessoas em um lugar só.', 'Resposta_Errada_2': 'As 3 pessoas vão se juntar as 2 pessoas e vamos ter 3 pessoas em um lugar só.'}

        erros= 0

        while True:
            if erros == 3:
                print('Você errou 3 vezes, tente novamente depois.')
                erros -= 3
                break

            escolhas=[]

            while True:
                opcoes=['Resposta_Certa', 'Resposta_Errada', 'Resposta_Errada_2']
                escolhendo_respostas= random.choice(opcoes)
                if len(escolhas) == 3:
                    break
                if escolhendo_respostas not in escolhas:
                    escolhas.append(escolhendo_respostas)

            print(f'1- {respostas[escolhas[0]]}\n2- {respostas[escolhas[1]]}\n3- {respostas[escolhas[2]]}')

            respondendo= input('Qual dessas é a alternativas correta? ')

            if   respondendo == '1' and escolhas[0] == 'Resposta_Certa':
                print('Resposta correta parabéns\n')
                break
            elif respondendo == '2' and escolhas[1] == 'Resposta_Certa':
                print('Resposta correta parabéns\n')
                break
            elif respondendo == '3' and escolhas[2] == 'Resposta_Certa':
                print('Resposta correta parabéns\n')
                break

            elif respondendo == '1' and escolhas[0] == 'Resposta_Errada':
                print('Resposta errada\n')
                erros += 1
            elif respondendo == '2' and escolhas[1] == 'Resposta_Errada':
                print('Resposta errada\n')
                erros += 1
            elif respondendo == '3' and escolhas[2] == 'Resposta_Errada':
                print('Resposta errada\n')
                erros += 1

            elif respondendo == '1' and escolhas[0] == 'Resposta_Errada_2':
                print('Resposta errada\n')
                erros += 1
            elif respondendo == '2' and escolhas[1] == 'Resposta_Errada_2':
                print('Resposta errada\n')
                erros += 1
            elif respondendo == '3' and escolhas[2] == 'Resposta_Errada_2':
                print('Resposta errada\n')
                erros += 1

            else:
                print('Essa opção não existe, por favor responda a pergunta com 1, 2 ou 3')
    
    else:
        print('Responda Sim com S e Não com N')

    print('\n Para fazer conta de subtração também é fácil, o sinal de subtração é esse (-), imagine que você tenha 2 maçãs na mesa, mas você está com fome e come 1 maçã, logo você tera 1 maçã pois a outra você comeu. Agora vamos imaginar que você tenha 5 bananas e você come 2 bananas, então você tera 3 bananas, já que você comeu 2 bananas das 5 que você tinha.\n\n  Para fazer conta de subtração, o número maior sempre vai está do lado esquerdo da conta e o numero menor vai ficar do lado direito da conta (5 - 2 = 3) ou se você preferir, você também pode fazer a conta em pé, aonde você vai colocar o numero maior na parte de cima da conta e o menor na parte de baixo da conta.\n\n para fazer esse tipo de conta você vai pegar o menor numero e vai contar de trás pra frente começando com o maior número, exemplo 10 - 5, você vai contar 5 de trás pra frente começando com o número 10.\n')

    print('Vamos ver se você aprendeu, responda essa pergunta.\n\nSe eu tenho 4 laranjas e eu comi 2 laranjas, quantas laranjas eu vou ter?')

    interesse= input('Você quer tentar responder a pergunta?\n[S] Sim\n[N] Não\n>> ').lower()
    if interesse == 'n':
        print('...')
    elif interesse == 's':
        erros= 0
        while True:
            if erros == 3:
                print('Você errou 3 vezes, por favo rê leia o texto para aprender novamente e depois volte a tentar.')
                break

            respostas= {'Resposta_Correta': 'Eu vou ficar com 2 laranja pois eu tinha 4 e comi 2', 'Resposta_errada': 'Eu vou ficar com 3 laranja pois eu tinha 4 e comi 2', 'Resposta_errada_2': 'Eu vou ficar com 1 laranja pois eu tinha 4 e comi 2'}
            opcoes= []

            while True:
                resposta= ['Resposta_Correta', 'Resposta_errada', 'Resposta_errada_2']
                escolhendo_respostas= random.choice(resposta)
                if len(opcoes) == 3:
                    break

                elif escolhendo_respostas not in opcoes:
                    opcoes.append(escolhendo_respostas)
            
            print(f'1- {respostas[opcoes[0]]}\n2- {respostas[opcoes[1]]}\n3- {respostas[opcoes[2]]}')

            respondendo= input('Qual dessas opções estão certas? ')

            if   respondendo == '1' and opcoes[0] == 'Resposta_Correta':
                print('Você acertou parabéns\n')
                erros= 0
                break
            elif respondendo == '2' and opcoes[1] == 'Resposta_Correta':
                print('Você acertou parabéns\n')
                erros= 0
                break
            elif respondendo == '3' and opcoes[2] == 'Resposta_Correta':
                print('Você acertou parabéns\n')
                erros= 0
                break
            
            elif respondendo == '1' and opcoes[0] == 'Resposta_errada':
                print('Você errou a resposta\n')
                erros += 1
            elif respondendo == '2' and opcoes[1] == 'Resposta_errada':
                print('Você errou a resposta\n')
                erros += 1
            elif respondendo == '3' and opcoes[2] == 'Resposta_errada':
                print('Você errou a resposta\n')
                erros += 1
            
            elif respondendo == '1' and opcoes[0] == 'Resposta_errada_2':
                print('Você errou a resposta\n')
                erros += 1
            elif respondendo == '2' and opcoes[1] == 'Resposta_errada_2':
                print('Você errou a resposta\n')
                erros += 1
            elif respondendo == '3' and opcoes[2] == 'Resposta_errada_2':
                print('Você errou a resposta\n')
                erros += 1
                
            else:
                print('Essa opção não existe, por favor escolha 1, 2 ou 3')

    else:
        print('Responda Sim com S e Não com N')

    return 