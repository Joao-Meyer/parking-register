from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conectar banco
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estacionamento"
)

@app.route("/")
def hello():
    return jsonify({
        "mensagem": "olamundo"
    })

# Lista as vagas
@app.route('/vagas')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vagas")
    vagas = cursor.fetchall()
    cursor.close()
    return render_template('index.html', vagas=vagas)

# Lista uma vaga específica
@app.route('/vagas/<int:id>')
def pegar_vaga(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vagas WHERE id = %s", (id,))
    vaga = cursor.fetchone()
    cursor.close()
    if vaga:
        return render_template('vaga.html', vaga=vaga)
    return jsonify({'erro': 'Não tem essa vaga '})

# Adicionar vaga
@app.route('/vagas/nova', methods=['GET', 'POST'])
def nova_vaga():
    if request.method == 'POST':
        posicao = request.form['posicao']
        ocupada = request.form.get('ocupada', False) == 'on'
        nome = request.form['nome']
        ondeesta = request.form['ondeesta']
        cursor = db.cursor()
        cursor.execute("INSERT INTO vagas (posicao, ocupada, nome, ondeesta) VALUES (%s, %s, %s, %s)", (posicao, ocupada, nome, ondeesta))
        db.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        return render_template('nova.html')

# Atauliza uma vaga
@app.route('/vagas/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar_vaga(id):
    if request.method == 'POST':
        posicao = request.form['posicao']
        ocupada = request.form.get('ocupada', False) == 'on'
        nome = request.form['nome']
        ondeesta = request.form['ondeesta']
        cursor = db.cursor()
        cursor.execute("UPDATE vagas SET posicao = %s, ocupada = %s, nome = %s, ondeesta = %s WHERE id = %s", (posicao, ocupada, nome, ondeesta, id))
        db.commit()
        cursor.close()
        return redirect(url_for('pegar_vaga', id=id))
    else:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vagas WHERE id = %s", (id,))
        vaga = cursor.fetchone()
        cursor.close()
        if vaga:
                return render_template('atualizar.html', vaga=vaga)
        return jsonify({'erro': 'Não tem essa vaga '})

# Apagar vaga
@app.route('/vagas/apagar/<int:id>')
def delete_vaga(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM vagas WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

app.run(host="0.0.0.0", port=3000, debug=True)