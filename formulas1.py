from Textos1 import texto1, apresentando_formulas, soma_subtracao, numeros_negativos, Multiplicacao_divisão
from Transformandoconta14 import fazendo_conta

numeros= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sinais=  ['+', '-']
sinais_errado= ['*', '/']

while True:
    print(texto1())
    resposta_usuario= input('Aperte enter para continuar\nou\nAperte 0 e enter para sair\n>> ')

    if resposta_usuario == '':
        while True:
            print(f'0- Volta\n{apresentando_formulas()}')
            resposta_usuario= input('Escolha uma das opções e logo em seguida der enter>> ')

            if resposta_usuario == '0':
                print('saindo...')
                break
        
            elif resposta_usuario == '1':
                print(soma_subtracao())
                while True:
                    resposta_usuario= input('Quer ultilizar uma calculadora para fazer uma conta de soma (+) ou subtração (-)?\n[S] sim\n[N] Não\n>>> ').lower()
                    
                    if resposta_usuario == 'n':
                        print('...')
                        break
                    
                    elif resposta_usuario == 's':
                        print('Lembrando que o maior número vem primeiro, depois o sinal (+ ou -) e por utimo o número menor')
                        conta= input('digite a sua conta>>> ').replace(',', '.')

                        numero_esquerdo= ''
                        numero_direito= ''
                        sinal_conta= ''
                        sinal_numero_negativo= ''

                        quantidade_de_caracteres= 0

                        for caracteres in conta:
                            if quantidade_de_caracteres == 0 and caracteres in sinais:
                                print('\n Depois você aprenderar fazer conta com números com sinais, por favor coloque números positivos (3) ao inves de números com sinais (-3 ou +3) para fazer a conta.\n\nColoque primeiro sempre o número maior e após o sinal coloque o número menor.\n')
                                break

                            if caracteres in numeros:
                                if sinal_conta == '':
                                    numero_esquerdo += caracteres
                                else:
                                    numero_direito += caracteres
                                    if quantidade_de_caracteres == len(conta)-1:
                                        try:
                                            numero_esquerdo= int(numero_esquerdo)
                                        except ValueError:
                                            numero_esquerdo= float(numero_esquerdo)
                                        
                                        try:
                                            numero_direito= int(numero_direito)
                                        except ValueError:
                                            numero_direito= float(numero_direito)
                                        
                                        if numero_direito > numero_esquerdo:
                                            print('\nPor favor colocar o número maior primeiro e depois do sinal o número menor.\n')
                                            break

                                        print(fazendo_conta(conta).Realizando_conta())

                            elif caracteres == '.':
                                if quantidade_de_caracteres == len(conta)-1:
                                    print('Por favor, presta um pouco mais de atenção, não coloque ponto ou virgula no fim da conta')
                                    break

                                elif sinal_conta == '':
                                    numero_esquerdo += caracteres
                                
                                else:
                                    numero_direito += caracteres

                            elif caracteres in sinais:

                                if numero_direito != '':
                                    print('\nDepois nos vamos aprender a fazer contas com mais de dois números, por favor coloque uma conta com um número no lado esquerdo, depois um sinal de soma (+) ou subtração (-) no meio e no lado direito um número final, para fazer a conta.\n')
                                    break

                                elif quantidade_de_caracteres == len(conta)-1:
                                    print('\nPor favor coloque um número depois do sinal de soma (+) ou depois do sinal de subtração (-) para conseguir fazer a conta. Não da pra resolver uma conta de soma (+) ou de subtração (-) com apenas 1 número.\n')
                                    break

                                elif sinal_conta == '':
                                    sinal_conta += caracteres

                                else:
                                    print('\nPor favor colocar apenas um sinal para fazer a conta de soma (+) ou a de subtração (-)\n')
                                    break
                            
                            elif caracteres in sinais_errado and numero_esquerdo != '':
                                print('\nAqui estamos fazendo apenas contas de soma (+) e subtração (-), então por favor faça contas utilizando um desses sinais\n')
                                break

                            elif caracteres not in numeros and caracteres != ' ':
                                print('\nPor favor colocar números\n')
                                break

                            quantidade_de_caracteres += 1

                    else:
                        print('\nEssa opção não existe.\n')
            
            elif resposta_usuario == '2':
                print(numeros_negativos())
                while True:
                    interesse= input('Você quer usar uma calculadora que te ajuda com esse conteúdo?\n[S] sim\n[N] nao\n>>> ').lower()
                    if interesse == 'n':
                        print('...')
                        break
                    
                    elif interesse == 's':
                        numero_esquerdo= ''
                        numero_direito= ''
                        sinal_conta= ''
                        sinal_numero_negativo= ''

                        quantidade_de_caracteres= 0
                        
                        conta= input('Por favor coloca aqui a sua conta>>> ').replace(',', '.')

                        for caracteres in conta:
                            
                            if caracteres == ' ':
                                pass
                            
                            elif caracteres == '.':
                                if sinal_conta == '':
                                    numero_esquerdo += caracteres
                                else:
                                    numero_direito += caracteres
                            
                            elif caracteres in sinais and numero_direito != '':
                                print('Aqui é apenas permitido uma conta com dois número, exemplo, 1 + 1')
                                break

                            elif caracteres in numeros and numero_direito != '':
                                print('Aqui é apenas permitido uma conta com dois número, exemplo, 1 + 1')
                                break
                            
                            elif caracteres == '+' and sinal_conta != '' or quantidade_de_caracteres == 0 and caracteres == '+':
                                print(' Não precisa colocar um sinal positivo (+) para indicar que o número é positivo, ele com ou sem sinal já é positivo a menos que você coloque um sinal negativo (-), ai o número se torna um número negativo')
                                break
                            
                            elif quantidade_de_caracteres == 0 and caracteres == '-':
                                numero_esquerdo += caracteres

                            elif numero_direito != '' and caracteres in sinais:
                                print(' Por favor coloque apenas dois número na conta')
                                break
                            
                            elif conta in sinais:
                                print(' Oh meu a amigo(a), como você quer fazer a conta sem sinal? vai tenta de novo e ve se coloca um sinal de + para somar ou de - para subtrair')
                                break
            
                            elif numero_esquerdo == '' and caracteres in sinais:
                                print(' Eita meu mano, eu acho que você esqueceu de colocar um numero no inicio para você fazer a conta.')
                                break

                            elif caracteres in numeros:
                                if sinal_conta == '':
                                    numero_esquerdo += caracteres
                                else:
                                    numero_direito += caracteres

                                    if quantidade_de_caracteres == len(conta)-1:
                                        try:
                                            numero_esquerdo= int(numero_esquerdo)
                                        except ValueError:
                                            numero_esquerdo= float(numero_esquerdo)
                        
                                        try:
                                            numero_direito= int(numero_direito)
                                        except ValueError:
                                            numero_direito= float(numero_direito)
                                        
                                        print(fazendo_conta(conta).Realizando_conta())
                            
                            elif caracteres in sinais and numero_esquerdo != '':
                                sinal_conta += caracteres

                            elif caracteres == '-' and sinal_conta != '':
                                numero_direito += caracteres
                            
                            else:
                                print(' Por favor coloque apenas números')
                                break


                            quantidade_de_caracteres += 1

                    else:
                        print('Por favor responda apenas com S sim e N para não')
            
            elif resposta_usuario == '3':
                print(Multiplicacao_divisão())
                    
        
    elif resposta_usuario == '0':
        print('saindo...')
        break

    else:
        print('Por favor certifiquise de que não tenha nada escrito ou certifiquise de que você não tenha apertado espaço, após isso aperte enter para continuar.')