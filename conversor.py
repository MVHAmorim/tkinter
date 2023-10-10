from tkinter import *

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def delEntry():
    entrada.delete(0, END)

def imprimirConversao():
    if isnumber(entrada.get()):
        print(f"""
            {entrada.get()} centímetros é igual a: {float(entrada.get()) / 100} metro(s)
            """)
        delEntry
    
janela = Tk()
janela.geometry("600x200")
janela.resizable(False, False)

#Widgets

#labels
titulo = Label(text = "Conversor de Centímetros para Metros",
               fg = "black",
               bg = "red")

texto = Label(text = "Informe a medida em centímetros:")

#entrys
entrada = Entry(fg = "#2a2a2a",
                bg = "#f3e8e8",
                width = 30)

#botões
enviar = Button(janela, text="Converter", command=imprimirConversao)

#definindo localização
titulo.pack()
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
titulo.place(x=200, y=50)

texto.pack()
texto.grid(row=1, column=0, padx=10, pady=5)
texto.place(x=100, y=100)

entrada.pack(side="left", padx=10, pady=5)
entrada.grid(row=2, column=0, padx=10, pady=5)
entrada.place(x=300, y=100)

enviar.pack(side="left", padx=10, pady=5)
enviar.grid(row=3, column=0, columnspan=5, padx=10, pady=5)
enviar.place(x=200, y=150)

janela.mainloop()
