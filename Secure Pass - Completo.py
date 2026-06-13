import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import json
import os

ARQUIVO = "passwords.json"

class SecurePassManager:

    def __init__(self, root):
        self.root = root
        self.root.title("SecurePass Manager")
        self.root.geometry("700x500")

        self.criar_interface()

    def criar_interface(self):

        titulo = tk.Label(
            self.root,
            text="🔒 SecurePass Manager",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=10)

        frame_gerador = tk.LabelFrame(
            self.root,
            text="Gerador de Senhas"
        )
        frame_gerador.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_gerador, text="Tamanho").grid(row=0, column=0)

        self.tamanho = tk.Entry(frame_gerador)
        self.tamanho.insert(0, "12")
        self.tamanho.grid(row=0, column=1)

        self.resultado = tk.Entry(
            frame_gerador,
            width=40
        )
        self.resultado.grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(
            frame_gerador,
            text="Gerar Senha",
            command=self.gerar_senha
        ).grid(row=2, column=0, columnspan=2)

        frame_cadastro = tk.LabelFrame(
            self.root,
            text="Cadastrar Credencial"
        )
        frame_cadastro.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_cadastro, text="Serviço").grid(row=0, column=0)
        tk.Label(frame_cadastro, text="Login").grid(row=1, column=0)

        self.servico = tk.Entry(frame_cadastro)
        self.login = tk.Entry(frame_cadastro)

        self.servico.grid(row=0, column=1)
        self.login.grid(row=1, column=1)

        tk.Button(
            frame_cadastro,
            text="Salvar",
            command=self.salvar_credencial
        ).grid(row=2, column=0, columnspan=2)

        self.tabela = ttk.Treeview(
            self.root,
            columns=("servico", "login"),
            show="headings"
        )

        self.tabela.heading("servico", text="Serviço")
        self.tabela.heading("login", text="Login")

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.carregar_tabela()

    def gerar_senha(self):

        try:
            tamanho = int(self.tamanho.get())

            caracteres = (
                string.ascii_letters +
                string.digits +
                string.punctuation
            )

            senha = ''.join(
                random.choice(caracteres)
                for _ in range(tamanho)
            )

            self.resultado.delete(0, tk.END)
            self.resultado.insert(0, senha)

        except:
            messagebox.showerror(
                "Erro",
                "Digite um número válido."
            )

    def carregar_dados(self):

        if os.path.exists(ARQUIVO):
            with open(ARQUIVO, "r") as arquivo:
                return json.load(arquivo)

        return []

    def salvar_dados(self, dados):

        with open(ARQUIVO, "w") as arquivo:
            json.dump(
                dados,
                arquivo,
                indent=4
            )

    def salvar_credencial(self):

        dados = self.carregar_dados()

        dados.append({
            "servico": self.servico.get(),
            "login": self.login.get(),
            "senha": self.resultado.get()
        })

        self.salvar_dados(dados)

        messagebox.showinfo(
            "Sucesso",
            "Credencial salva!"
        )

        self.carregar_tabela()

    def carregar_tabela(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for dado in self.carregar_dados():

            self.tabela.insert(
                "",
                "end",
                values=(
                    dado["servico"],
                    dado["login"]
                )
            )

root = tk.Tk()
app = SecurePassManager(root)
root.mainloop()