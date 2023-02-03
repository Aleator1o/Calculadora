class Conta(object):
    def __init__(self, n1= None):
        self.n1= n1 #conta do usuario.
        self.q= 0 #para selecionar as chaves que vai fazer a conta.

    def soma(self):
        self.q -= self.q #para garantir que self.q seja igual a 0.

        result= [] #Copiá da conta do usuario aonde vai ficar o resultado final da soma de todos os números.
        result1= [] #recebe o(s) resultado(s) da(s) conta(s).

        result= self.n1.copy() #envia uma copiá da conta do usuario para o result, assim evitando perdade de dados no processo do cálculo.
        
        while True:
            if len(result) == 1:
                #Finaliza a conta quando a soma de todos os números forem feitos, e o resultado final ser o unico item da lista result.
                break

            elif str(len(result)/2)[2] != '0':

                """Caso a quantidades de item na lista seja igual a um número 
                ímpar, exemplo, caso dentro de result tenha 3 itens ([1, 23, 1])
                o utimo item da lista vai ser mandado para o result1 e apagado da
                lista result, para que assim o result tenha um número par de itens,
                evitando o erro de procurar um item que não existe."""

                result1.append(result[len(result)-1])
                del result[len(result)-1]
            
            nresult= result[0] + result[1] #Fazendo a soma
            result1.append(nresult) #Enviando o resultado para o result1, para fazer a soma com outros resultados.
            del result[0:2] #Removendo os números que já foram usados para fazer o resultado de uma soma, e evitar resultados repetidos.

            if len(result) == 0:

                """Qunado todas as somas forem feitas e os resultados estiverem no
               result1, o programa vai pegar todos os resultados e passa para o result
               para fazer a soma dos resultados, até que sobre um resultado de uma soma
               que sera mandada para o result como o resultado final de toda conta feita,
               de todos os resultados.
               
               E é claro que após ele passar os resultados para a lista result, todos os
               resultados que estiverem na lista result1, seram apagados para que possa ser
               feito novas contas, sem puxar os resultados repetidos."""

                result= result1.copy()
                del result1[:]
            
        return result[0] #mostra o resultado da soma final de todos os números.
    
    def subtracao(self):
        rs= self.soma()

        rs -= self.n1[0]
        result= self.n1[0] - rs

        return result

    def divisao(self):
        self.q -= self.q
        result= []
        result1= []
        
        result= self.n1.copy()

        nresult= result[0]/result[1]
        result1.append(nresult)

        del result[0:2]

        if len(result) > 0:
            while True:
                nresult= result1[self.q] / result[self.q]
                result1.append(nresult)

                if self.q == len(result)-1:
                    break

                self.q += 1
         
        return float(f'{result1[len(result1)-1]:.2F}')
    
    def multiplicacao(self, re= None):
        self.q -= self.q
        self.re= re

        result=[]
        result1=[]

        if re == None:
            result= self.n1.copy()
        else:
            result= self.re.copy()
        
        while True:
            if len(result) == 1:
                break

            elif len(result) > 39:
                for c in range(40, len(result)):
                    print(c)
                    result1.append(result[c])

                del result[40:len(result)]

            elif str(len(result)/2)[2] != '0':
                result1.append(result[len(result)-1])
                del result[len(result)-1]

            #print(len(result)/2, '\n', result, '\n', result[self.q], result[self.q+1])
            nresult= result[self.q] * result[self.q+1]
            result1.append(nresult)
            
            if self.q+1 == len(result)-1:
                del result[:]
                result= result1.copy()
                del result1[:]
                self.q -= self.q

            elif len(result) > 2:
                self.q += 2

        return result[0]
    
    #completar codigo de expoente (o codigo de expoente exige apenas dois numeros)
    def expoente(self):
        self.q -= self.q
        result=[]
        result= self.n1.copy()
        result1=[]
        for c in range(0, result[1]):
            result.append(result[0])
        del result[0:2]
        nresult= self.multiplicacao(result)
        del result[0:len(result)-1]
        return nresult
            #3^3 +/* 3^4= 3^3+4= 3^7
    #Adcionar conta de raiz
    
        

