import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///books.db")

ANOS = [i for i in range(1950, 2031)]

GENEROS = ["Ficção", "Auto-ajuda", "História", "Política e Sociedade", "Religião", "Informática", "Finanças", "Medicina e Saúde", "Administração e Negócios", "Direito e Legislação", "Geografia e Geopolítica"]

STATUSS = ["Quero Ler", "Lendo", "Lido", "Abandonado"]

NOTAS = [0, 1, 2, 3, 4, 5]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/incluirlivro", methods=["GET", "POST"])
def incluirlivro():
        return render_template("incluirlivro.html", anos=ANOS, generos=GENEROS, statuss=STATUSS, notas=NOTAS)

@app.route("/consultarlivro", methods=["GET", "POST"])
def consultarlivro():
        registers = db.execute("SELECT * FROM books")
        return render_template("register.html", registers=registers)

@app.route("/deletarlivro", methods=["GET", "POST"])
def deletarlivro():
        id = request.args.get("deletar")
        db.execute("DELETE FROM books WHERE id = ?", id)
        registers = db.execute("SELECT * FROM books")
        return render_template("register.html", registers=registers)

@app.route("/include", methods=["POST"])
def include():
    ano = request.form.get("ano")
    if not ano:
        return render_template("error.html", message="Missing ano")
    titulo = request.form.get("titulo")
    if not titulo:
        return render_template("error.html", message="Missing titulo")
    autor = request.form.get("autor")
    if not autor:
        return render_template("error.html", message="Missing autor")
    genero = request.form.get("genero")
    if not genero:
        return render_template("error.html", message="Missing genero")
    status = request.form.get("status")
    if not status:
        return render_template("error.html", message="Missing status")
    nota = request.form.get("nota")

    db.execute("INSERT INTO books (ano, titulo, autor, genero, status, nota) VALUES(?, ?, ?, ?, ?, ?)", ano, titulo, autor, genero, status, nota)

    return redirect("/registers")

@app.route("/registers")
def registers():
    registers = db.execute("SELECT * FROM books")
    return render_template("register.html", registers=registers)