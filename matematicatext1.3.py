from matematica12 import Conta

conta_usuario= input('Digite a sua conta >>> ').strip()

class fazendo_conta(object):
    def __init__(self):
        self.identificador_de_numeros= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.identificador_de_sinais= ['+', '-', '*', '/']
        self.conta_usuario_separado= []
        self.conta_separado= []
        self.conta_final= []

        self.conta= Conta(self.conta_final)

        self.numero_e= ''
        self.numero_d= ''
        self.sinal= ''

        self.identificador_numero_caractere= 0
        self.verificando_sinais_principais= True

    def Realizando_conta(self):
        def Fazendo_conta():
            
            self.sinal= sinal
                        
            self.conta_final.append(self.conta_separado[self.identificador_numero_caractere-1])
            self.conta_final.append(self.conta_separado[self.identificador_numero_caractere+1])
                        
            del self.conta_separado[self.identificador_numero_caractere+1]
            del self.conta_separado[self.identificador_numero_caractere]
            del self.conta_separado[self.identificador_numero_caractere-1]

            if len(self.conta_separado) == 0:
                            
                self.conta_separado.append(self.Contas())
                del self.conta_final[:]
                self.sinal= ''
                        
            elif len(self.conta_separado) > 0:
                            
                self.conta_separado.insert(0, self.Contas())
                del self.conta_final[:]
                self.sinal= ''

        self.Transformando_conta()
        self.conta_separado= self.conta_usuario_separado.copy()
        while True:
            
            if len(self.conta_separado) == 1:
                break

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
                
                del self.conta_separado[self.identificador_numero_caractere+1]
                del self.conta_separado[self.identificador_numero_caractere]
                del self.conta_separado[self.identificador_numero_caractere-1]
                
                if self.identificador_numero_caractere > len(self.conta_separado)-1:
                    
                    self.conta_separado.append(self.Contas())
                    del self.conta_final[:]
                    self.sinal= ''
                    
                else:
                    
                    self.conta_separado.insert(self.identificador_numero_caractere-1, self.Contas())
                    del self.conta_final[:]
                    self.sinal= ''

        return self.conta_separado[0]

    
    def Transformando_conta(self):
        for caracteres in conta_usuario:

            if caracteres in self.identificador_de_numeros:
                if self.sinal == '':
                    self.numero_e += caracteres

                else:
                    self.numero_d += caracteres
                    if self.identificador_numero_caractere == len(conta_usuario)-1:
                        self.conta_usuario_separado.append(int(self.numero_d))
                   
            elif caracteres in self.identificador_de_sinais:
                if self.numero_d != '':
                    self.conta_usuario_separado.append(int(self.numero_d))
                    self.conta_usuario_separado.append(caracteres)
                    self.sinal= caracteres
                    self.numero_d= ''

                else:
                    self.sinal= caracteres
                    self.conta_usuario_separado.append(int(self.numero_e))
                    self.conta_usuario_separado.append(self.sinal)
            self.identificador_numero_caractere += 1
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

textando= fazendo_conta()
print(textando.Realizando_conta())
