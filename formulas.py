from Textos import texto1, apresentando_formulas, soma_subtracao
from matematicatext14 import fazendo_conta

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
                        conta= input('digite a sua conta>>> ')

                        numero_esquerdo= ''
                        numero_direito= ''
                        sinal_conta= ''
                        sinal_numero_negativo= ''

                        numeros= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                        sinais=  ['+', '-']
                        sinais_errado= ['*', '/']

                        quantidade_de_caracteres= 0

                        for caracateres in conta:
                            if quantidade_de_caracteres == 0 and caracateres in sinais:
                                print('\n Depois você aprenderar fazer conta com números com sinais, por favor coloque números positivos (3) ao inves de números com sinais (-3 ou +3) para fazer a conta.\n\nColoque primeiro sempre o número maior e após o sinal coloque o número menor.\n')
                                break

                            if caracateres in numeros:
                                if sinal_conta == '':
                                    numero_esquerdo += caracateres
                                else:
                                    numero_direito += caracateres
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

                            elif caracateres == '.':
                                if sinal_conta == '':
                                    numero_esquerdo += caracateres
                                
                                else:
                                    numero_direito += caracateres

                            elif caracateres in sinais:

                                if numero_direito != '':
                                    print('\nDepois nos vamos aprender a fazer contas com mais de dois números, por favor coloque uma conta com um número no lado esquerdo, depois um sinal de soma (+) ou subtração (-) no meio e no lado direito um número final, para fazer a conta.\n')
                                    break

                                elif quantidade_de_caracteres == len(conta)-1:
                                    print('\nPor favor coloque um número depois do sinal de soma (+) ou depois do sinal de subtração (-) para conseguir fazer a conta. Não da pra resolver uma conta de soma (+) ou de subtração (-) com apenas 1 número.\n')
                                    break

                                elif sinal_conta == '':
                                    sinal_conta += caracateres

                                else:
                                    print('\nPor favor colocar apenas um sinal para fazer a conta de soma (+) ou a de subtração (-)\n')
                                    break
                            
                            elif caracateres in sinais_errado and numero_esquerdo != '':
                                print('\nAqui estamos fazendo apenas contas de soma (+) e subtração (-), então por favor faça contas utilizando um desses sinais\n')
                                break

                            elif caracateres not in numeros and caracateres != ' ':
                                print('\nPor favor colocar números\n')
                                break

                            quantidade_de_caracteres += 1

                    else:
                        print('\nEssa opção não existe.\n')

        
    elif resposta_usuario == '0':
        print('saindo...')
        break

    else:
        print('Por favor certifiquise de que não tenha nada escrito ou certifiquise de que você não tenha apertado espaço, após isso aperte enter para continuar.')