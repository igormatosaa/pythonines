import numpy as calculo

import matplotlib.pyplot as grafico

import tkinter as tk

tela = tk.Tk()
tela.geometry("500x500")
tela.title("o_O")

upperLimit = tk.Label(tela,text = "upperLimit:").grid(column=0,row=0,padx=5,pady=5)
upperLimitInput = tk.Entry().grid(column=1,row=0)

underLimit = tk.Label(tela,text = "underLimit:").grid(column=0,row=1,padx=5,pady=5)
underLimitInput = tk.Entry().grid(column=1,row=1,padx=5,pady=5)

numeroTrapezios = tk.Label(tela,text='Numero de Trapézios:').grid(column=0,row=2,padx=5,pady=5)
numeroTrapeziosInput = tk.Entry().grid(column=1,row=2,padx=5,pady=5)

numeroCasasDecimais = tk.Label(tela,text="Numero de Casas Decimais:").grid(column=0,row=3,padx=5,pady=5)
numeroCasasDecimaisInput = tk.Entry().grid(column=1,row=3,padx=5,pady=5)




tela.mainloop()

