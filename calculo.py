import numpy as calculo

import math

class calculos():

    def arrumaString(expressao):
        expressao = expressao.replace('sqrt', 'calculo.sqrt')

        expressao = expressao.replace('loge', 'calculo.log')

        expressao = expressao.replace('log2', 'calculo.log2')

        expressao = expressao.replace('log10', 'calculo.log10')

        expressao = expressao.replace('sen', 'calculo.sin')

        expressao = expressao.replace('cos', 'calculo.cos')

        expressao = expressao.replace('^', '**')

        return expressao

    def tabelaString(array):
        x_string = ""
        for i in range (len(array)):
            if i<len(array)-1:
                x_string = x_string + str(array[i]) + "\n"
            else : x_string = x_string + str(array[i])
        return x_string
    
    def respostaIntervalos(total,erro,casas):
        intervalo_menor = total - float(erro)
        intervalo_maior = total + float(erro)

        intervalo_menor = calculos.my_round(intervalo_menor, casas+2)
        intervalo_maior = calculos.my_round(intervalo_maior, casas+2)

        intervalo_string = "[" + str(intervalo_menor) + " ; " + str(intervalo_maior) + "]"
        intervalo_string = intervalo_string + "\n" + "ou (" + str(total) + "±" + str(erro) + ")"
        return intervalo_string

    def my_round(n, ndigits):
        part = n * 10 ** ndigits
        delta = part - int(part)
        if delta >= 0.5 or -0.5 < delta <= 0:
            part = math.ceil(part)
        else:
            part = math.floor(part)
        return part / (10 ** ndigits) if ndigits >= 0 else part * 10 ** abs(ndigits)
    
    def trapez(y,casas,passo):
        total = 0
        tamanho = len(y)-1
        for i in range (len(y)):
            if i==0 or i==tamanho:
                total += y[i]/2
                total = calculos.my_round(total, casas)
            else : 
                total += y[i]

        total = total*passo
        total = calculos.my_round(total, casas)
        return total


    def calcular(inicio,fim,N,passo,casas_decimais,expressao):

        inicio = int(inicio)
        fim = int(fim)
        casas_decimais = int(casas_decimais)

        if N != "":
            N = int(N)
            passo = (fim-inicio)/N
        elif N == "" and passo != "":
            passo = float(passo)
            N = (fim-inicio)/passo
            N = int(N)

        x = calculo.linspace(inicio,fim,N,endpoint=False)

        x = calculo.append(x,fim)

        expressao = calculos.arrumaString(expressao)

        f_x = eval(expressao)

        potencia_de_dez = 10**(-(casas_decimais+1))
        taxa_erro = 5 * potencia_de_dez

        erro_arredondamento = N*taxa_erro*passo

        y = f_x

        y = calculo.round(y,casas_decimais)
        
        erro_arredondamento = format(erro_arredondamento, f".{casas_decimais + 1}f")
        
        total = calculos.trapez(y,casas_decimais,passo)

        erro_conta_string = str(N) + " *(5*10^" + str(casas_decimais+1) + ")* " + str(passo)
        erro_arredondamento_string = erro_arredondamento
        tabela_x = calculos.tabelaString(x)
        tabela_f_x = calculos.tabelaString(y)
        resposta_soma_trap = str(total)
        resposta_intervalos = calculos.respostaIntervalos(total,erro_arredondamento,casas_decimais)

        array_strings = [tabela_x,tabela_f_x,resposta_soma_trap,resposta_intervalos,erro_arredondamento_string,erro_conta_string,x,f_x]

        return array_strings