import numpy as calculo

import matplotlib.pyplot as grafico

def arrumaString(expressao):
    expressao = expressao.replace('sqrt', 'calculo.sqrt')

    expressao = expressao.replace('loge', 'calculo.log')

    expressao = expressao.replace('log2', 'calculo.log2')

    expressao = expressao.replace('log10', 'calculo.log10')

    expressao = expressao.replace('sen', 'calculo.sin')

    expressao = expressao.replace('cos', 'calculo.cos')

    expressao = expressao.replace('tan', 'calculo.tan')

    return expressao

def formatar(resultado, casas_decimais):
    return format(resultado, f".{casas_decimais}f")


grafico.style.use(['dark_background'])

N = 6
x = calculo.linspace(2,5,N,endpoint=False)

x = calculo.append(x,5)

y = calculo.array([0,0])

print(x)

expressao = input()

expressao = arrumaString(expressao)

print(expressao)

f_x = eval(expressao)

grafico.plot(x,f_x,'x-')

erro_arredondamento = (5*(10**-)

y[0]=x[0]

total_valor = calculo.array([])

valor = f_x
print(valor)

total = calculo.trapz(f_x,x)

total = calculo.round(total, 5)

casas_decimais = 5

total = formatar(total, casas_decimais)

print(f" o valor e {total} ")

grafico.show()