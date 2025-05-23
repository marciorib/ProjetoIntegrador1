# Projeto Integrador I — Sistema de Cadastro e Controle de Reclamações

Este projeto foi desenvolvido como parte do Projeto Integrador da faculdade, em parceria com a empresa Carrier Logística, com o objetivo de digitalizar e otimizar o processo de registro e acompanhamento de reclamações recebidas por meio de órgãos de defesa do consumidor (como FA e CIP).


## Objetivos

Centralizar as informações de reclamações em uma plataforma web intuitiva, eliminando a necessidade de registros manuais em planilhas Excel, reduzindo retrabalho, ruídos de comunicação e acelerando a resposta aos clientes e órgãos reguladores.


## Tecnologias Utilizadas

### Backend
- **Python**: lógica de negócio, gerenciamento de rotas e manipulação de dados.
- **Flask**: servidor e APIs REST.
- **SQLite**: armazenamento estruturado de dados.

### ORM: 
- **SQLAlchemy**

### Frontend
- **HTML5**: estruturação dos conteúdos da página.
- **CSS3**: estilização da interface.
- **Bootstrap**: responsividade e layout.


## Funcionalidades

- [x] Cadastro de reclamações (FA/CIP).
- [x] Listagem de todas as reclamações com indicadores:
  -  Total de reclamações
  -  Reclamações pendentes
  -  Reclamações resolvidas
- [x] Atualização do status da reclamação (pendente/resolvida)
- [x] Interface web amigável para operadores.
- [x] Armazenamento seguro e centralizado dos dados.
- [x] Base de dados estruturada para análise estatística futura


## Instalação e Execução

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes)

### 1. Clone o repositório

```bash
git clone https://github.com/marciorib/ProjetoIntegrador1.git
```
### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o .env
Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
```bash
DATABASE_URL=sqlite:///reclamacoes.db
SECRET_KEY=secret_key
```

### 4. Execute a aplicação
```bash
python app.py
```
Acesse no navegador: http://localhost:5000