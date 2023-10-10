from tkinter import *

def delEntry():
    entrada.delete(0, END)

def imprimirSaudacao():
    print(f"""
          Seja bem vindo {entrada.get()},
          Como estão seus estudos?
          """)
    delEntry
    
janela = Tk()
#Widgets

#labels
titulo = Label(text = "INFINITY SCHOOL",
               fg = "black",
               bg = "red")

nome_label = Label(text = "Insira seu nome")

#entrys
entrada = Entry(fg = "#2a2a2a",
                bg = "#f3e8e8",
                width = 30)

#botões
enviar = Button(janela, text="submit", command=imprimirSaudacao)

#definindo localização
titulo.pack()
titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
titulo.place(x=200, y=50)

nome_label.pack()
nome_label.grid(row=1, column=0, padx=10, pady=5)
nome_label.place(x=100, y=100)

entrada.pack(side="left", padx=10, pady=5)
entrada.grid(row=1, column=0, padx=10, pady=5)
entrada.place(x=300, y=100)

enviar.pack(side="left", padx=10, pady=5)
enviar.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
enviar.place(x=200, y=150)

janela.mainloop()