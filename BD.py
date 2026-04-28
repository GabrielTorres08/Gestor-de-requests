import sqlite3
from rich import print
import os

class DB_ADM:
    def __init__(self):
        pass

    def __init__(self):
        self.con = sqlite3.connect(os.environ['CONECT_DB'], check_same_thread=False)
        self.cur = self.con.cursor()

    def existeBD(self, user):
        self.cur.execute("SELECT 1 FROM clientes WHERE id = ? LIMIT 1", (user,))
        existe = self.cur.fetchone()
        return existe
    
    def pegarDados(self, user):
        try:
            self.cur.execute(f"SELECT * FROM clientes WHERE id = {(user)}")
            email = self.cur.fetchone()
            return email

        except sqlite3.Error as e:
            print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")

    def pegarEmail(self, user):
        try:
            self.cur.execute(f"SELECT email FROM clientes WHERE id = {(user)}")
            email = self.cur.fetchone()
            email = email[0]
            return email

        except sqlite3.Error as e:
            print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")


    def inserirDados(self, user, nome, email, idade, admin):
        try:
            self.cur.execute("INSERT INTO clientes (id, nome, email, idade, admin ) VALUES (?,?,?,?,?)",(user, nome, email, idade, admin))
            self.con.commit()
            print("Dados adicionados")
        except sqlite3.Error as e:
            print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")

    def deletarComId(self,user):
        try:
            self.cur.execute(f"DELETE FROM clientes WHERE id = {(user)}")
            self.con.commit()
            print("Dados deletados")
        except sqlite3.Error as e:
            print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")

    def criarTabela(self,nome_tabela):
        try:
            self.cur.execute(f'''
                CREATE TABLE IF NOT EXISTS {nome_tabela} (
                    id INTEGER UNIQUE,
                    nome TEXT NOT NULL,
                    email TEXT UNIQUE,
                    idade INTEGER,
                    admin BOOLEAN NOT NULL CHECK (admin IN (0, 1))
                    )''')
            self.con.commit()
            print(f"Tabela '{nome_tabela}' criada!")

        except sqlite3.Error as e:
            print(f"\n[bold yellow]ERRO:[/bold yellow] [bold red]{e}[/bold red]\n")