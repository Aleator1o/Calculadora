import random

def texto1():
    return '\n  Olá usuario, sejá bem vindo ao revisando conhecimento matemático, o programa ainda está em desenvolvimento, então por favor não se chatei caso de algum erro no programa, nos avise caso você encontrar um error no programa, logo em seguida você será reconpensado após checarmos o erro que você nos sitou.\n Aqui escolha uma fórmula matemática para revisar os seus conhecimentos ou aprender algo novo, apos escolher uma opção aperte enter para continuar.\n'

def apresentando_formulas():
    return '1- soma e subtração.\n2- Números negativos.\n3- Multiplicação e divisão\n*- soma e subtração com mais de dois números.'

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

    return ''

def numeros_negativos():
    print('\n Aqui nós vamos aprender sobre os números negativos, os números negativos são números que ficam a baixo de 0 e para represeta-los você verar ele com esse sinal (-) atrás do número, exemplo -4, -3, -2, -1, 0, 1, 2, 3, 4. Veja os números negativos como se você estivesse devendo um dinheiro que você não tem a uma pessoa, e toda vez que você da uma quantia menor da qual você está devendo a pessoa, o número negativo ele diminui, por exemplo, eu estou devendo 10RS a um amigo mas eu não tenho o dinheiro para pagar ele, logo eu tenho -10 RS, e um dia eu ganhei 5RS e vou lá pagar a minha divida e dou os meus 5RS para ele, logo vou DIMINUIR a minha divida de -10RS para -5RS, e no dia seguinte eu dou a ele mais 5RS e a minha divida com ele de -5RS vai cair para 0RS e não vou está devendo mais nada para ele.\n\n Agora vamos supor que eu peguei 10RS com o meu amigo e não paguei ele, vou fica com -10RS com ele, só que no dia seguinte eu vou lá e pego mais 5RS com ele e não pago a ele os 10RS que eu já devia e nem os 5RS que peguei com ele, assim eu vou ficar devendo ao meu amigo 15RS, me deixando com -15RS, e sempre que eu estiver com um número negativo e da um número postivo a esse número negativo, o número nagativo vai diminuindo por que ele vai se tornando um número positivo, e sempre que eu vou dando um número negativo ao número positivo, aos poucos o número positivo vai diminuindo até virar um número que vai ficar A BAIXO DE ZERO e se tornar um número negativo, espero que tenha entendido.\n\n Vamos fazer algumas contas, vamos supor que eu tenha 10RS e vou usar todos esses 10RS para pagar uma divida de 6RS, a conta seria assim -6 + 10, e você contaria assim, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, desconsiderando o número 0 da contagem, eu paguei toda a minha divida e ainda me sobrou 4RS. se eu estivesse devendo 30RS a alguem e pagasse com 40RS, eu estaria com -30RS com aquela pessoa, porém iria pagar com os meu 40RS, logo a conta ficaria assim -30 + 40, e você contaria assim, -30, -29, -28, -27... e iria diminuir o número negativo 40 vezes até chegar no número zero, sem considerar ele na contagem, que seria aonde você começaria a aumentar os números positivos, ...-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, e então no fim eu ficaria com 10RS.\n\n E porque eu davo fazer a contagem sem considerar o número zero 0? Simples o número eles dão representatividade a quantidade, então se eu tenho uma quantidade de coisas coisas, essa quantidade seria representado por um número, e o número zero ele representa nenhuma quantidade, o número zero é um indincador de que ali não tem nada, e é por isso que agente não considera o número zero, pq ele diz que ali não tem nada, e se tivesse alguma coisa isso seria representado por algum outro número que considerariamos na contagem.\n\n Bom agente falou mais de números negativos indo para o números positivos, agora vamos falar um pouco mais de números positivos virando números negativos, para isso vamos supor que nos tem 10RS e colocamos o mesmo numa aposta, só que nessa aposta se a gente perde a gente perde o dobro do que colocamos, e no fim agente perdeu, e 20RS sendo que só temos 10RS, e para fazer mos essa conta ficaria assim 10 + -20, alias a ordem dos número não interfere no resultado, logo você contaria assim, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, e então ainda estariamos devendo 10RS, ficando com -10RS. Espero que tenha pegado a ideia.\n\n Vamos tentar resolver uma conta, se eu tenho 15RS e estou te devendo 30RS e te dou os 15RS para pagar parte da minha divida, quantos reais eu ainda vou ficar te devendo?')

    erros= 0

    while True:
        interesse= input('Você quer responder a conta?\n[S] Sim\n[N] Não\n>>> ').lower()

        if interesse == 'n':
            print('...')
            erros -= erros
            break
        
        elif interesse == 's':
            if erros == 3:
                print('Você errou três vezes, tente denovamente de pois.')
                erros -= 3
                break

            resposta= input('Com quantos reais eu vou ficar?\nPor favor colocar apenas números >>> ')

            if resposta == '-15' or resposta == '-15RS' or resposta == '-15 reais':
                print('Parabéns você acertou')
                erros -= erros
                break

            else:
                print('Resposta errada')
                erros += 1

        else:
            print('Essa opção não existe')
    
    print(' Agora vamos tocar em um assunto importante na subtração, no assunto passado eu pedi para você colocar o número maior no lado esquerdo e o número menor no lado direito, por que você tiria que remover do número esquerdo uma quantidade superior a ele mesmo, o que resultaria em um número negativo.\n\n Pois se você colocasse o número menor no lado esquerdo e o maior no lado direito, você teria que fazer uma contagem que daria um número negativo, e você não iria saber como fazer isso, sendo que é so falar o número normalmente do número positivo até o 0 e da li você iria voltar a aumentar o número só que no final você iria colocar um número negativo, pois você ainda vai está diminuido e quando você aumenta o número so que no negativo, você continua diminuindo, bom o importante é que agora você sabe.\nVamos, tente responder quanto da 4 - 5?')

    while True:
        interesse= input('Você quer responder?\n[S] Sim\n[N] Não\n>>> ').lower()
        if interesse == 'n':
            print('...')
            break

        elif interesse == 's':
            resposta= input('Responde utilizando apenas números>>> ')
            
            if erros == 3:
                print('Você errou 3 vezes tente novamente depois')
                break
            
            elif resposta == '-1':
                print('Parebéns você acertou')
                break

            else:
                erros += 1
                print(f'Você errou tente novamente, você tem apenas {erros}/3 tentativas')
        
        else:
            print('Coloque apenas para S para sim e N para não')
    
    return ''

def Multiplicacao_divisão():
    print(' As contas de multiplicação e divisão é relativamente facíl isso depende muito do seu nivel de esforço e vontade de querer aprender, bom vamos começar com multiplicação, bom todo número multiplicado vai ser somado a ele mesmo por uma quantidade de vezes de número qualquer, por exemplo, 2 x 2 == 4 ou 2+2= 4 ou 10 x 5= 50 ou 10 + 10 + 10 + 10 + 10= 50, como no exemplo agente vai pegar o número do lado esquerdo e soma com ele mesmo a quantidade de vezes do número do lado direito, entendeu? bom espero que sim, nesse caso vamo dificultar um pouco.\n\n Vamos lembrar que aqui, não importa o lado que você vá fazer a sua conta, o resultado vai ser o mesmo, e você também pode fazer a conta em pé assim como no exemplo abaixo\n\n12\nx3\n\n Ok, agora vamos lembra-los de que para fazer as contas de multiplicação é recomendado você por o maior número na parte de cima e o menor número na parte de baixo, pois assim facilita na hora de fazer a conta e você a termina mais rapido, e para fazer a conta de multiplicação com 2 digitos na parte de cime e 1 digito na parte de baixo como no exemplo acima, você vai primeiro multiplicar o três (O número de baixo) pela quantidade de vezes do primeiro digito do número de cima sendo a ordem da direita para esquerda, nesse caso você pegaria o três e primeiro multiplicaria com o número 2 e colocaria o resultado em baixo assim:\n\n12\nx3\n 6\n\n E logo ao lado esquerdo do 6 você vai continuar a conta com o resultado de 3 x 1, um número multiplicado por 1 é igual a ele mesmo, nesse caso 3 x 1 o resultado é igual a ele mesmo e nesse caso a resposta seria 3, todo número multiplicado por ele mesmo é igual a ele mesmo, e aproveitando esse momento vim lembra-los de que todo número multilplicado por 0 é e sempre serar igual a 0, após achar o resultado nós vamos coloca-lo no lado direito do 6, ficando assim:\n\n12\nx3\n36\n\n Agora vamos fazer essa mesma conta so que ao contrario, vamos pegar o 3 e vamos colocar em cima e vamos pegar o 12 e colocar em baixo assim:\n\n  3\nx12\n\n para resolver multiplicação desse jeito tbm é facil. Primeiro para resolver as contas de multiplicação nos sempre vai começar da direita para a esquerda, nesse caso a gente vai começar multiplicando o 2 pelo 3 e logo em seguida a gente vai multiplicar o 1 pelo 3. Agora veja em baixo da conta linhas orizontais equivalentes a quantidades de digitos que tem no número de baixo, nesse caso me referindo ao número 12 do número de cima o número 3, cada linha vai pertencer a um digito do número de baixo, o número 12, lembrando que a conta é sempre feita da direita pra esquerda, então a primeira linha que você vai colocar a resposta vai ser do digito 2 do número 12, o número de baixo até você te multiplicado o 2 com todos os número de cima, nesse caso apenas com o 3, após você terminar de multiplicar o primeiro digito do número do baixo com o primeiro digito do número de cima, você vai pegar a respota e coloca-lo na sua linha de resposta, como é o primeiro digito da direita para a esquerda, você vai pegar a resposta e colocar em baixo da conta na primeira linha, agora veja uma linha vertical entre todos os números e reto passando na conta toda até mesmo na parte das linhas orizontais aonde fica as respostas, isso deve fazer uns quadradinhos em baixo da conta, cada quadradinho você vai colocar uma respota, como por exemplo a multiplicação do 2 vezes o 3, pelo o dois ser o primeiro digito do número de baixo do sentido da direita para a esquerda sabemos que a resposta vai ser na primeira linha, e como é o primeiro digito do número de cima da direita para a esquerda o mesmo vai ficar no primeiro quadrado da direita para a esquerda da primeira linha, espero que até aqui você já tenha pegado a ideia do que eu disse e do que eu quero dizer até agora, se você não está conseguindo imaginar nada do que eu disse até agora, sugiro que você comece de novo e desenhe em um papel ou comece a ler livros sem figuras e imagine em sua mente todas as cenas escrita no papel. Bom a sua conta deve esta mais ou menos assim sem as linhas\n\n  3\nx12\n  6\n\n Bom, feito a primeira conta agora nos vamos fazer a segunda conta, que é com o segundo digito do número de baixo, com o primeiro digito do número de cima, lembrando que agente so vai passa para o proximo digito do número de baixo, depois de termos feitos a multiplicação desse digito com todos os digitos de cima, ai quando tiver feito todas as multiplicações do digito de baixo com todos do de cima, a sim você começa a multiplicar o proximo digito do número de baixo com todos os de cima, colocando sempre a resposta na linha orizontal que pertence ao mesmo, exemplo, se você vai multiplicar o primeiro digito de baixo da direita para a esquerda, a resposta deve ser colocado na primeira linha orizontal em baixo da conta, depois de ter feito todas as multiplicações do primeiro digito do número de baixo com todos os número de cima, você vai para o proximo digito ou se você preferir vá para o segundo digito do número de baixo na ordem da direita para a esquerda, a(s) resposta(s) da(s) multiplicação vai para a proxima linha orizontal em baixo da conta e assim por diante, também lembrando que as proximas respostas vão ficar um quadrado a mais do ultimo quadrado, vamo supor que você terminou a primeira conta e começou colocando a primeira resposta no primeiro quadrado da direita para a esquerda, na proxima conta na linha de beixo, ao invez de você começa colocar a resposta pelo o primeiro quadrado, você vai começar a colocar a resposta pelo o proximo quadrado depois do anterior, e assim por diante. Agora vamos para a proxima conta que se você está pretando atenção vai saber que a proxima conta vai ser 1 x 3 e se você ta realmente prestando a tenção e notando, não necessariamente notando para lembrar, vai saber a respota em um instante, e se você responder 1 você errou, a resposta na verdade é 3 por que você não vai somar o 3 com outro 3 e nem algo do tipo, ta mais para como se você somasse 1 + 1 + 1 do que 3 + 0, se bem que somar um número mais 0 toda vez que o mesmo for multiplicado por 1 é bem mais facil, mas não me inventa de responder 2 em uma multiplicação de 1 x 1 por que um número multiplicado por ele mesmo é ele, nesse caso você somaria 1 + 0 que da 1. Após pegar essa respota você vai colocar em seu devido lugar que você ja deve saber aonde fica, que é em baixo da ultima respota uma casa a mais para a esquerda e a sua conta deve ficar mais ou menos assim sem as linhas:\n\n  3\nx12\n  6\n 3\n\n Bom agora que você tem toda feita, ainda tem um ultimo passo que deve ser feito, a soma do resultados das multiplicações, você vai fazer a soma da seguinte forma, primeiro você vai pegar o primeiro digito das respotas da direita para a esquerda e vai somar com o número de baixo, caso não tenha um número você so passa o número para baixo e assim por diante com o todos os números da direita para a esquerda, a sua conta deve terminar assim:\n\n  3\nx12\n  6\n 3\n 36\n\n E é isso, agora tente você resolver essa conta de multiplicação 12 x 12')

    interesse= input('Você quer responder a esse pergunta?\n[S] Sim\n[N] Não\n>>> ').lower()

    erros= 0

    if interesse == 'n':
        print('...')
    
    elif interesse == 's':
        while True:
            respota= int(input('Digite aqui a resposta e apenas números: ')) #264

            if erros == 3:
                print('Você errou três vezes por favo tente novamente depois.')
                erros -= erros
                break
            
            elif respota == 264:
                print(f'parabéns você acertou {erros}/3')
                erros -= erros
                break
            
            elif respota != int:
                print('Por favor coloque apenas números e sem pontos ou virgulas')
            
            elif respota != 264:
                erros += 1
                print(f'você errou tente de novo {erros}/3')
    else:
        print('Por favor coloque S para sim e N para não.')
    
    print('Agora vamos aprender divisão...')

def soma_subtracao_avancado():
    print('\n Bom antes de falarmos um pouco sobre, vamos relembrar algumas coisas, como por exemplo, sempre que agente for fazer uma conta qualquer que seja, ela sempre começa da esquerda e vai indo para a direita, exemplo 1 + 2 - 4, primeri vamos fazer a conta 1 + 2 que vai da 3, e depois vamos pegar esse resultado e subtrair com o ultimo número da conta que é 4, que o resultado no final vai ser 1.\n\n Aqui você pode começar a colocar números pequenos primeros e depois números grandes.\n\n Bom para fazer esse tipo de conta você tem que lembrar que ela começa da esquerda indo para direita, logo se a conta é 3 - 2 + 4 - 3, você vai começar fazendo a conta de subtração 3 - 2, e o resultado vai fica no lugar dessa conta, então a conta segueria assim 1 + 4 - 3, e então você vai passa para a proxima conta que é 1 + 4, e o resultado que é 5 vai ficar no lugar dessa conta, e a sua conta vai da continuidade assim 5 - 3, e então você vai fazer a conta, e o resultado que é 2 vai ser o resultado de toda a conta 3 - 2 + 4 - 3.')

    print('Vamos ver se você entendeu.\n\n Escreva essa seguinte conta num papel 3 + 2 - 4 + 3 e tente resolver, lembrando que se você quiser, pode ir pular as perguntas')

    while True:

        interesse= input('Você quer responder essa pergunta?\n[S] Sim\n[N] Não\n>>> ').lower()

        if interesse == 'n':
            print('...')
            break
        
        elif interesse == 's':
            resposta= input('Qual é a resposta>> ')

            if resposta == '4':
                print('Parebéns você acertou')
                break
            
            else:
                print('Você errou')
        
        else:
            print("Digite 's' para responder e 'n' para não responder.")
    
    return ''