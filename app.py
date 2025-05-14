
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# ✅ Criar a instância do banco de dados
db = SQLAlchemy(app)

# Modelos
class Reclamante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

class Reclamacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(255))
    resolvido = db.Column(db.Boolean, default=False)
    reclamante_id = db.Column(db.Integer, db.ForeignKey('reclamante.id'))
    reclamante = db.relationship('Reclamante', backref='reclamacoes')

# Rotas
@app.route('/')
def index():
    return redirect(url_for('listar'))

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        titulo = request.form['titulo']
        descricao = request.form['descricao']

        # Verifica se já existe o reclamante
        reclamante = Reclamante.query.filter_by(email=email).first()
        if not reclamante:
            reclamante = Reclamante(nome=nome, email=email)
            db.session.add(reclamante)
            db.session.commit()

        nova_reclamacao = Reclamacao(
            titulo=titulo,
            descricao=descricao,
            reclamante_id=reclamante.id
        )

        db.session.add(nova_reclamacao)
        db.session.commit()
        return redirect(url_for('listar'))

    return render_template('cadastrar.html')

@app.route('/listar')
def listar():
    total_reclamacoes = Reclamacao.query.count()
    pendentes = Reclamacao.query.filter_by(resolvido=False).count()
    resolvidas = Reclamacao.query.filter_by(resolvido=True).count()
    reclamacoes = Reclamacao.query.all()
    return render_template(
        'listar.html',
        reclamacoes=reclamacoes,
        total_reclamacoes=total_reclamacoes,
        pendentes=pendentes,
        resolvidas=resolvidas
    )

@app.route('/atualizar_status/<int:id>', methods=['POST'])
def atualizar_status(id):
    reclamacao = Reclamacao.query.get_or_404(id)
    reclamacao.resolvido = not reclamacao.resolvido
    db.session.commit()
    return redirect(url_for('listar'))

# Execução
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
