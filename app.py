from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/reclamacoes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelos
class Reclamante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    reclamacoes = db.relationship('Reclamacao', backref='reclamante', lazy=True)

class Reclamacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    reclamante_id = db.Column(db.Integer, db.ForeignKey('reclamante.id'), nullable=False)

@app.route('/')
def index():
    return redirect(url_for('listar_reclamacoes'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        reclamante = Reclamante.query.filter_by(email=email).first()
        if not reclamante:
            reclamante = Reclamante(nome=nome, email=email)
            db.session.add(reclamante)
            db.session.commit()

        nova_reclamacao = Reclamacao(titulo=titulo, descricao=descricao, reclamante_id=reclamante.id)
        db.session.add(nova_reclamacao)
        db.session.commit()
        return redirect(url_for('listar_reclamacoes'))

    return render_template('cadastrar.html')

@app.route('/listar')
def listar_reclamacoes():
    reclamacoes = Reclamacao.query.all()
    return render_template('listar.html', reclamacoes=reclamacoes)

# Execução
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
