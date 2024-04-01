import matplotlib.pyplot as grafico

import calculo as integrar

import tkinter as tk

def calcular(inicio,fim,N,passo,casas,expressao):
    return integrar.calculos.calcular(inicio,fim,N,passo,casas,expressao)

def getLegenda():
    legenda = "loge(x)\nlog10(x)\nlog2(x)\nsqrt(x)\nsen(x)\ncos(x)\ntan(x)"
    return legenda

def novaJanela(inicio,fim,N,passo,casas,expressao):
    array_strings = calcular(inicio,fim,N,passo,casas,expressao)

    if array_strings != []:
    
        tela_respostas = tk.Tk()
        frame = tk.Frame(tela_respostas)
        tela_respostas.geometry("320x320")
        tela_respostas.title("Respostas")
        
        x_label = tk.Label(tela_respostas,text="x").grid(column=0,row=0,padx=5,pady=5)

        f_x_label = tk.Label(tela_respostas,text="f(x)").grid(column=1,row=0,padx=5,pady=5)

        tabela_x =  tk.Label(tela_respostas,text=array_strings[0]).grid(column=0,row=1,padx=5,pady=5)

        tabela_f_x =  tk.Label(tela_respostas,text=array_strings[1]).grid(column=1,row=1,padx=5,pady=5)

        resposta_soma_trap = tk.Label(tela_respostas,text=f"Soma das areas dos Trapezios:\n{array_strings[2]}").grid(column=0,row=2,padx=5,pady=5)
        
        resposta_intervalos = tk.Label(tela_respostas,text=f"Intervalo:\n{array_strings[3]}").grid(column=0,row=3,padx=5,pady=5)
        
        erro_arredondamento = tk.Label(tela_respostas,text=f"Erro arredondamento:\n{array_strings[4]}").grid(column=1,row=2,padx=5,pady=5)

        erro_conta = tk.Label(tela_respostas,text=f"Calculo do erro:\n{array_strings[5]}").grid(column=1,row=3,padx=5,pady=5)

        grafico.style.use(['dark_background'])
        grafico.plot(array_strings[6],array_strings[7],'x-')
        grafico.show()

        tela_respostas.mainloop()

tela = tk.Tk()
tela.geometry("420x300")
tela.title("Entradas")
tela.resizable(False,False)

upper_limit = tk.Label(tela,text = "Fim:").grid(column=0,row=0,padx=5,pady=5)
upper_limit_input = tk.Entry()
upper_limit_input.grid(column=1,row=0)

under_limit = tk.Label(tela,text = "Inicio:").grid(column=0,row=1,padx=5,pady=5)
under_limit_input = tk.Entry()
under_limit_input.grid(column=1,row=1,padx=5,pady=5)

numero_trapezios = tk.Label(tela,text='Numero de Trapézios:').grid(column=0,row=2,padx=5,pady=5)
numero_trapezios_input = ""
numero_trapezios_input = tk.Entry()
numero_trapezios_input.grid(column=1,row=2,padx=5,pady=5)

valor_passo = tk.Label(tela,text='Passo:').grid(column=0,row=3,padx=5,pady=5)
valor_passo_input = ""
valor_passo_input = tk.Entry()
valor_passo_input.grid(column=1,row=3,padx=5,pady=5)

numero_casas_decimais = tk.Label(tela,text="Numero de Casas Decimais:").grid(column=0,row=4,padx=5,pady=5)
numero_casas_decimais_input = tk.Entry()
numero_casas_decimais_input.grid(column=1,row=4,padx=5,pady=5)

expressao_label = tk.Label(tela,text="Digite a expressao:").grid(column=0,row=5,padx=5,pady=5)
expressao_input = tk.Entry()
expressao_input.grid(column=1,row=5,padx=5,pady=5)

legendas_label = tk.Label(tela,text=getLegenda()).grid(column=2,row=0,padx=30,pady=5,rowspan=4)

botao = tk.Button(tela,text="integrar",command=lambda: novaJanela(under_limit_input.get(),
                                                                upper_limit_input.get(),
                                                                numero_trapezios_input.get(),
                                                                valor_passo_input.get(),
                                                                numero_casas_decimais_input.get(),
                                                                expressao_input.get()))
botao.grid(column=1,row=6,padx=5,pady=5)                                                                           

tela.mainloop()

