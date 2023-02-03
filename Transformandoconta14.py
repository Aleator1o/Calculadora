from calculadora13 import Conta

class fazendo_conta(object):
    def __init__(self, conta_usuario):
        self.conta_usuario= conta_usuario
        self.identificador_de_numeros= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.identificador_de_sinais= ['+', '-', '*', '/']
        self.identificador_tipo_numero=[float, int]
        self.conta_usuario_separado= []
        self.conta_separado= []
        self.conta_final= []

        self.conta= Conta(self.conta_final)

        self.numero_e= ''
        self.numero_d= ''
        self.sinal= ''

        self.identificador_numero_caractere= 0
        self.verificando_sinais_principais= True
        self.contas_principais= False

    def Realizando_conta(self):
        def Fazendo_conta():
            
            self.sinal= sinal
                        
            self.conta_final.append(self.conta_separado[self.identificador_numero_caractere-1])
            self.conta_final.append(self.conta_separado[self.identificador_numero_caractere+1])

            if self.contas_principais == True:
                print('Agora que fizermos a(s) outra(s) conta(s) primerio, vamos fazer a(s) conta(s) de soma e a de subtração.')
            
            else:
                print('Então vamos fazer a(s) conta(s) de soma ou a de subtração.')
            
            if self.conta_separado[self.identificador_numero_caractere] == '+':
                print(f'Nesse caso vamos fazer a soma de {self.conta_separado[self.identificador_numero_caractere-1]} + {self.conta_separado[self.identificador_numero_caractere+1]} que da.')

            elif self.conta_separado[self.identificador_numero_caractere] == '-':
                print(f'Então vamos fazer a subtração do número {self.conta_separado[self.identificador_numero_caractere-1]} - {self.conta_separado[self.identificador_numero_caractere+1]} que da.')

                        
            del self.conta_separado[self.identificador_numero_caractere+1]
            del self.conta_separado[self.identificador_numero_caractere]
            del self.conta_separado[self.identificador_numero_caractere-1]

            if len(self.conta_separado) == 0:
                            
                resultado= self.Contas()
                self.conta_separado.append(resultado)
                del self.conta_final[:]
                self.sinal= ''

                print(resultado, '\nE agora vamos colocar esse resultado no lugar dos números e do sinal que foram utilizado para chegar nesse resultado.')
                        
            elif len(self.conta_separado) > 0:
                            
                resultado= self.Contas()
                self.conta_separado.insert(self.identificador_numero_caractere-1, resultado)
                del self.conta_final[:]
                self.sinal= ''

                print(resultado, '\nE agora vamos colocar esse resultado no lugar dos números e do sinal que foram utilizado para chegar nesse resultado.')

        self.Transformando_conta()
        print("Bom vamos começar a fazer a conta")
        self.conta_separado= self.conta_usuario_separado.copy()
        while True:
            if len(self.conta_separado) == 1:
                print(f'E o resultado final de toda essa conta foi')
                break

            mostrando_conta= ''
            for caracteres in self.conta_separado:
                if type(caracteres) == int or type(caracteres) == float:
                    mostrando_conta += str(caracteres)
                
                else:
                    mostrando_conta += caracteres
                
                mostrando_conta += ' '
            print(mostrando_conta)

            self.identificador_numero_caractere= 0
            
            if self.verificando_sinais_principais == True:
                
                for sinal in self.conta_separado:
                    self.verificando_sinais_principais= False
                    
                    if sinal == '*' or sinal == '/':
                        self.verificando_sinais_principais= True
                        self.sinal= sinal
                        break
                    
                    self.identificador_numero_caractere += 1
            elif self.verificando_sinais_principais == False:
                for sinal in self.conta_separado:
                    
                    if sinal == '+':
                        Fazendo_conta()
                        break
                        
                    if sinal == '-':
                        Fazendo_conta()
                        break
                    
                    self.identificador_numero_caractere += 1
                    
            if self.verificando_sinais_principais == True:
                
                self.conta_final.append(self.conta_separado[self.identificador_numero_caractere-1])
                self.conta_final.append(self.conta_separado[self.identificador_numero_caractere+1])

                print('Como sempre vamos fazer antes da conta de soma e subtração, a conta de multiplicação e divisão.')
                if self.conta_separado[self.identificador_numero_caractere] == '*':
                    print(f'E vamos fazer a conta {self.conta_separado[self.identificador_numero_caractere-1]} * {self.conta_separado[self.identificador_numero_caractere+1]} que da.')
                    self.contas_principais= True
                    
                elif self.conta_separado[self.identificador_numero_caractere] == '/':
                    print(f'E vamos fazer a conta {self.conta_separado[self.identificador_numero_caractere-1]} / {self.conta_separado[self.identificador_numero_caractere+1]} que da.')
                    self.contas_principais= True
                
                del self.conta_separado[self.identificador_numero_caractere+1]
                del self.conta_separado[self.identificador_numero_caractere]
                del self.conta_separado[self.identificador_numero_caractere-1]
                
                if self.identificador_numero_caractere > len(self.conta_separado)-1:

                    resultado= self.Contas()
                    self.conta_separado.append(resultado)
                    del self.conta_final[:]
                    self.sinal= ''

                    print(resultado, '\nE agora vamos colocar esse resultado no lugar dos números e do sinal que foram utilizado para chegar nesse resultado.')
                    
                else:
                    
                    resultado= self.Contas()
                    self.conta_separado.insert(self.identificador_numero_caractere-1, resultado)
                    del self.conta_final[:]
                    self.sinal= ''

                    print(resultado, '\nE agora vamos colocar esse resultado no lugar dos números e do sinal que foram utilizado para chegar nesse resultado.')

        return self.conta_separado[0]
    
    def Mudando_tipo_numero(self, numero):
        try:
            self.conta_usuario_separado.append(int(numero))
            
        except ValueError:
            self.conta_usuario_separado.append(float(numero))

    def identificando_numeros_negativos(self):
        self.identificador_numero_caractere= 0
        
        for caracteres in self.conta_usuario_separado:
            if self.conta_usuario_separado[0] == '-':
                self.conta_usuario_separado[0] += str(self.conta_usuario_separado[1])
                del self.conta_usuario_separado[1]

                try:
                    self.conta_usuario_separado.insert(0, int(self.conta_usuario_separado[0]))
                    del self.conta_usuario_separado[1]
                except ValueError:
                    self.conta_usuario_separado.insert(0, float(self.conta_usuario_separado[0]))
                    del self.conta_usuario_separado[1]
            
            elif caracteres == '-' and self.conta_usuario_separado[self.identificador_numero_caractere-1] in self.identificador_de_sinais:
                
                self.conta_usuario_separado[self.identificador_numero_caractere] += str(self.conta_usuario_separado[self.identificador_numero_caractere+1])
                del self.conta_usuario_separado[self.identificador_numero_caractere+1]

                try:
                    self.conta_usuario_separado.insert(self.identificador_numero_caractere, int(self.conta_usuario_separado[self.identificador_numero_caractere]))
                    del self.conta_usuario_separado[self.identificador_numero_caractere+1]
                
                except ValueError:
                    self.conta_usuario_separado.insert(self.identificador_numero_caractere, float(self.conta_usuario_separado[self.identificador_numero_caractere]))
                    del self.conta_usuario_separado[self.identificador_numero_caractere+1]

            self.identificador_numero_caractere += 1

        self.identificador_numero_caractere= 0
        return self.conta_usuario_separado

    def Transformando_conta(self):
        self.identificador_numero_caractere= 0

        for caracteres in self.conta_usuario:

            if caracteres == '.':
                if self.sinal == '':
                    self.numero_e += '.'
                
                else:
                    self.numero_d += '.'

            elif caracteres in self.identificador_de_numeros:
                if self.sinal == '':
                    self.numero_e += caracteres

                else:
                    self.numero_d += caracteres
                    if self.identificador_numero_caractere == len(self.conta_usuario)-1:
                        self.Mudando_tipo_numero(self.numero_d)
                   
            elif caracteres in self.identificador_de_sinais:
                if caracteres == '-' and self.identificador_numero_caractere == 0:
                    self.conta_usuario_separado.append(caracteres)

                elif self.numero_d != '':
                    self.Mudando_tipo_numero(self.numero_d)
                    self.conta_usuario_separado.append(caracteres)
                    self.sinal= caracteres
                    self.numero_d= ''

                else:
                    if caracteres == '-' and self.conta_usuario[self.identificador_numero_caractere-1] == ' ':
                        if self.conta_usuario[self.identificador_numero_caractere-2] in self.identificador_de_sinais:
                            self.conta_usuario_separado.append(caracteres)
                    
                    if self.sinal == '' and self.numero_e != '':
                        self.sinal= caracteres
                        self.Mudando_tipo_numero(self.numero_e)
                        self.conta_usuario_separado.append(self.sinal)
            
            self.identificador_numero_caractere += 1
            
        self.identificando_numeros_negativos()
        return self.conta_usuario_separado
    
    def Contas(self):
        if self.sinal == '+':
            return self.conta.soma()
        elif self.sinal == '-':
            return self.conta.subtracao()
        elif self.sinal == '*':
            return self.conta.multiplicacao()
        elif self.sinal == '/':
            return self.conta.divisao()


#conta= input('digite a sua conta >>> ')
#asd= fazendo_conta(conta)
#print(asd.Realizando_conta())