import tkinter as tk
from tkinter import messagebox

def opcao1():
    messagebox.showinfo("Opção 1", "Você selecionou a Opção 1!")

def opcao2():
    messagebox.showinfo("Opção 2", "Você selecionou a Opção 2!")

def opcao3():
    messagebox.showinfo("Opção 3", "Você selecionou a Opção 3!")


root = tk.Tk()
root.title("Menu Simples")


menu = tk.Menu(root)
root.config(menu=menu)

menu_arquivo = tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Opção 1", command=opcao1)
menu_arquivo.add_command(label="Opção 2", command=opcao2)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)

menu_ajuda = tk.Menu(menu)
menu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Este é um exemplo de menu em Tkinter."))
root.mainloop()