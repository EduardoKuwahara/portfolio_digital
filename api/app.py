from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/projetos')
def projetos():
    return render_template('projetos.html')
@app.route('/info')
def informacoes():
    return render_template('informacoes.html')

if __name__ == "__main__":
    app.run(debug=True)
