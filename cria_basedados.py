import sqlite3

conn = sqlite3.connect('basedados.db')
cursor = conn.cursor()

cursor.execute('''

create table cadastro_clientes(
    id integer primary key autoincrement,
    nome text not null,
    sobrenome text not null,
    cpf text not null
)

''')

cursor.execute('insert into cadastro_clientes(nome,sobrenome,cpf) values ("João", "Caviciolli", "12345678910")')
cursor.execute('insert into cadastro_clientes(nome,sobrenome,cpf) values ("Seu", "Madruga", "452634235456")')

conn.commit()
conn.close()