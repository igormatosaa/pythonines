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
fim = 5
inicio = 2

x = calculo.linspace(inicio,fim,N,endpoint=False)

x = calculo.append(x,fim)

y = calculo.array([0,0])

print(x)

expressao = input()

expressao = arrumaString(expressao)

print(expressao)

f_x = eval(expressao)

grafico.plot(x,f_x,'x-')

casas_decimais = 3
passo = (fim-inicio)/N
dez_elevado = 10**(-(casas_decimais+1))
cinco_virgulado = 5 * dez_elevado

erro_arredondamento = N*cinco_virgulado*passo

print()

y[0]=x[0]

total_valor = calculo.array([])

valor = f_x
print(valor)
erro_arredondamento = formatar(erro_arredondamento,casas_decimais)
print(f"a a {erro_arredondamento}")

total = calculo.trapz(f_x,x)

total = calculo.round(total, 5)

total = formatar(total, casas_decimais)

print(f" o valor e {total} ")

grafico.show()