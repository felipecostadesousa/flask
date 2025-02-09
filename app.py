from flask import Flask, render_template
from functions.get_arbitros import get_arbitros
from functions.get_competicoes import get_competicoes
from functions.get_titulos import get_titulos
from functions.get_localizacoes import get_localizacoes
from functions.get_times import get_times
from functions.get_estadios import get_estadios
from functions.get_tecnicos import get_tecnicos
from functions.get_jogadores import get_jogadores

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/competicoes")
def competicoes():
  competicoes = get_competicoes()
  return render_template("competicoes.html", competicoes=competicoes)

@app.route("/arbitros")
def arbitros():
  arbitros = get_arbitros()
  return render_template("arbitros.html", arbitros=arbitros)

@app.route("/titulos")
def titulos():
  titulos = get_titulos()
  return render_template("titulos.html", titulos=titulos)

@app.route("/localizacoes")
def localizacoes():
  localizacoes = get_localizacoes()
  return render_template("localizacoes.html", localizacoes=localizacoes)

@app.route("/estadios")
def estadios():
  estadios = get_estadios()
  return render_template("estadios.html", estadios=estadios)

@app.route("/times")
def times():
  times = get_times()
  return render_template("times.html", times=times)

@app.route("/tecnicos")
def tecnicos():
  tecnicos = get_tecnicos()
  return render_template("tecnicos.html", tecnicos=tecnicos)

@app.route("/jogadores")
def jogadores():
  jogadores = get_jogadores()
  return render_template("jogadores.html", jogadores=jogadores)

@app.route("/criar_titulo")
def criar_titulo():
  return render_template("criar_titulo.html")

@app.route("/editar_titulo")
def editar_titulo():
  return render_template("editar_titulo.html")

@app.route("/remover_titulo")
def remover_titulo():
  return render_template("remover_titulo.html")

if __name__ == "__main__":
  app.run(debug=True)