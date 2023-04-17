import tkinter as tk
import functions as f


def printvalue():
    print(f.getChoiceSetValue(choice))

window = tk.Tk()
window.geometry('1080x720')
window.title('SISTEMA DE VENDA')

choices = f.getProductsFromDb()
choice = tk.StringVar(window)
choice.set('escolha um produto')

w = tk.OptionMenu(window,choice,*choices)
w.place(x=330,y=200)

bttn = tk.Button(window,command=printvalue)
bttn.place(x=450,y=200)


windowTitle = tk.Label(window,text='SISTEMA DE COMPRA E VENDA',font='Cordana 20',justify='center')
windowTitle.place(x=330,y=100)




window.mainloop()