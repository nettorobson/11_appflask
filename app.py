# O app.py é o arquivi principal de configuração do projeto do Flask

# Isso é padrão:
from flask import Flask,render_template,request,url_for,redirect
import sqlite3

# Isso é padrão também:
app = Flask(__name__)

# Routes ou rotas (ou subdiretórios) são caminhos definidos dentro da estrutura da página para onde vai apontar.
# São cmainhos em uma aplicação web
# A página principal de uma aplicação WERB é também conhecido como "/" ou "raiz"

# No Flask, precisamos dizer qual é a ROUTE da página principal/inicial

#@app.route('/') # Função decoradora que já vai chamar a função abaixo quando abrir a raiz.
#def hello():
#    return "Olá Estou Executando a página inicial com FLASK"

# Importante
# Para rodarmos o que criamos com o FLASK.
# Lá no terminal:
# >>> (flaskenv2) (base) oppy@oppy-Aspire-A514-54G:~/Dell/Downloads/jcavi/backend/11_appflask$ export FLASK_APP=app
# >>> (flaskenv2) (base) oppy@oppy-Aspire-A514-54G:~/Dell/Downloads/jcavi/backend/11_appflask$ flask run


# Renderizando a página inicial com um template HTML

# Conexão com o banco da aula seguinte:
def get_db_connection():
    conn = sqlite3.connect('basedados.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index(): # Chamar de index é boa prática
    return render_template('index.html')

# Se rodar, vai retornar aviso que deu certo, indicando a porta 5000
# Se copiar o endereço que resultou em um navegador e ver o resultado.

@app.route('/clientes')
def clientes():
    return "Olá. Estou executando a página de Clientes"

# AULA 12
# Vamos importar lá em cima o sqlite3 para poder criar a função de conexão com o banco.
# Vamos lá em cima antes das rotas, criar a conexão com o banco na função 'def get_Db_connection():'

# Vamos agora criar as rotas para as outras URL do FrontEnd
# Para o FrontEnd se comunicar e interagir com o BackEnd, ele usa os métodos GET e POST.
# GET: busca informação do BackEnd e traz para a tela (ou para o FrontEnd)
# POST: Leva a informação inserida pelo usuário no FrontEnd, e leva para o BackEnd 
# Toda vez que o usuário acessa pela primeira vez, o método é o GET
# API usa muito os métodos GET e POST

@app.route('/listaclientes',methods=('GET','POST')) 
def listaclientes():
    conn = get_db_connection()
    clientesback = conn.execute('select * from cadastro_clientes').fetchall() # Essa informação, o nome da variável, já vem lá do Front. A integração é feita através de uma variável
    conn.close()
    return render_template('listaclientes.html',clientes=clientesback) # Essa variável interliga a front com o back (troca comunicação)

@app.route('/addclientes', methods=('GET','POST'))
def addclientes():
    if request.method == "POST": # Vamos ter que importar também a biblioteca request, url_for e redirect do FLASK.
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        conn = get_db_connection()
        conn.execute('insert into cadastro_clientes(nome,sobrenome,cpf) values (?,?,?)',(nome,sobrenome,cpf))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('addclientes.html') # Renderiza o html