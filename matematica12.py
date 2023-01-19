class Conta(object):
    def __init__(self, n1= None):
        self.n1= n1
        #para selecionar as chaves que vai fazer a conta
        self.q= 0
    def soma(self):
        #para garantir que q seja igual a 0
        self.q -= self.q
        #conta principal
        result= []
        #recebidor de todos os resultados dos calculos
        result1= []
        #enviador da primeira conta, para o result
        result= self.n1.copy()
        #toda a conta
        while True:
            #Soma completa
            #para finalizar a conta caso chegue no resultado final
            if len(result) == 1:
                break
            #caso o result receba um quantia que seja igual a um numero impar, e não causar erro
            elif str(len(result)/2)[2] != '0':
                result1.append(result[len(result)-1])
                del result[len(result)-1]
            #a soma
            nresult= result[self.q] + result[self.q+1]
            #enviador do resultado da conta nresult para o result1
            result1.append(nresult)
            #Quando toda as contas do result forem finalizadas
            if self.q+1 == len(result)-1:
               #apagar toda a lista para receber a continuação da conta
               del result[:]
               #enviador da proxima conta para o result
               result=result1.copy()
               del result1[:]
               #para não achar uma chave inesxistente do result
               self.q -= self.q
            #para ir para a proxima conta
            elif len(result) > 2:
                self.q += 2
        #mostra o resultado da conta
        return result[0]
    #codigo de subtração completo
    def subtracao(self):
        rs= self.soma()
        rs -= self.n1[0]
        result= self.n1[0] - rs
        return result
    #codigo de divisão completa
    def divisao(self):
        self.q -= self.q
        result=[]
        result= self.n1.copy()
        result1= []
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
    #codigo de multiplicação completo
    def multiplicacao(self, re= None):
        self.q -= self.q
        self.re= re
        result=[]
        if re == None:
            result= self.n1.copy()
        else:
            result= self.re.copy()
        result1=[]
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
            print(len(result)/2, '\n', result, '\n', result[self.q], result[self.q+1])
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
    
        

