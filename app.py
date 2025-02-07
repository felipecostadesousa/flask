from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/competicoes")
def competicoes():
  return render_template("competicoes.html")

@app.route("/arbitros")
def arbitros():
  return render_template("arbitros.html")

@app.route("/titulos")
def titulos():
  return render_template("titulos.html")

@app.route("/localizacoes")
def localizacoes():
  return render_template("localizacoes.html")

if __name__ == "__main__":
  app.run(debug=True)