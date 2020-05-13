# Sites usados para busca de informações
# https://www.sqlitetutorial.net/sqlite-python/
# https://docs.python.org/3/library/sqlite3.html

import sqlite3
from sqlite3 import Error
user_path =  r"C:\Users\Usuario\Desktop\KENNEDY\CRUD_LINX.db"
 
def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except Error as e:
		print(e)

def insert_cadastro(conn, cadastro):
	sql = "INSERT INTO cadastro(nome,idade,cidade) VALUES(?,?,?)"
	cur = conn.cursor()
	cur.execute(sql, cadastro)
	conn.commit()
	return cur.lastrowid

def update_cadastro(conn, cadastro):
	sql = "UPDATE cadastro SET nome=?, idade=?, cidade =? WHERE id=?"
	cur = conn.cursor()
	cur.execute(sql, cadastro)
	conn.commit()

def delete_cadastro( conn, id ):
	sql = 'DELETE FROM cadastro WHERE id=?'
	cur = conn.cursor()
	cur.execute(sql, (id,))
	conn.commit()

def show_cadastro(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM cadastro")
	
	rows = cur.fetchall()
	for row in rows:
		print( row )


def query_text(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM cadastro")
	
	result = cur.fetchall()
	
	c = open('CRUD_LINX.txt', 'w')
	
	for row in result:
		c.write(str(result))
		
	c.close()
	


def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print(sqlite3.version)
		sql = "CREATE TABLE IF NOT EXISTS cadastro("
		sql += "id INTEGER PRIMARY KEY AUTOINCREMENT,"
		sql += "nome VARCHAR(255) NOT NULL,"
		sql += "idade INTEGER,"
		sql += "cidade VARCHAR(255));"
		create_table(conn, sql)
			
		print('Olá, você está no serviço de atendimento ao cliente da Kennedy Soluções, ')
		print('por favor entre com os seus dados cadastrais para que possamos')
		print('atender a sua solicitação o quanto antes.')
		print('')
		
		try:
			nome = str(input("digite seu nome: "))
			idade = str(input("digite sua idade: "))
			cidade = str(input("digite sua cidade: "))
			cadastro = (nome, idade, cidade)
			insert_cadastro(conn, cadastro)
			
		except Error as e:
			print(e)
		
		print('')
		print('Perfeito' +' ' + nome + ', agora que você já está cadastrado em nosso sistema, o que deseja fazer?')
		print('Você deseja cadastrar um amigo (1), Listar os Cadastros da Base de Dados (2), Editar um cadastro da Base de '
			  'dados (3), ou Excluir um cadastro(4), ou Exportar a tabela para .txt(5)?')
		print('')
		
		user_input = int(input(''))
		print('')
		
		
		if int(user_input) == 1:
			print('Você escolheu registrar um amigo, por favor siga os passos abaixo para finalizar o cadastro.')
			create_connection(user_path)

		elif int(user_input) == 2:
			print('Você escolheu listar todos os cadastros disponíveis, aguarde um minuto que já lhe mostraremos tudo :)')
			
			print('')
			show_cadastro(conn)
			print('')
			
			print('Deseja realizar mais alguma coisa? Sim(1), Não(2)')
			final_choice = int(input(''))
					
			if int(final_choice) == 1:
				print('')
				create_connection(user_path)

			elif int(final_choice) == 2:
				print('Tudo bem :) nos vemos em breve então.')
				return

		elif int(user_input) == 3:
			print('Você escolheu editar um cadastro de nossa base, por favor indique o Índice dentre os abaixo que você pretende editar.')
			
			print('')
			show_cadastro(conn)
			print('')
			
			user_chose = int(input('Qual cadastro será atualizado? '))
			
			print('Certo, iremos atualizar o cadastro' +" "+str(user_chose)+ " " +', mas primeiro digite abaixo os novos valores que serão susbtituidos :)')
			new_nome = str(input("Digite o novo Nome: "))
			new_idade = str(input("Digite a nova Idade: "))
			new_cidade = str(input("Digite a nova Cidade: "))
			
			cadastro = (new_nome, new_idade, new_cidade, user_chose)
			update_cadastro(conn, cadastro)
			print('')
			
			print('Perfeito! Os dados foram atualizados com sucesso :)')
			print('')
			show_cadastro(conn)
			print('')
			
			print('Deseja realizar mais alguma coisa? Sim(1), Não(2)')
			final_choice = int(input(''))
					
			if int(final_choice) == 1:
				print('')
				create_connection(user_path)

			elif int(final_choice) == 2:
				print('Tudo bem :) nos vemos em breve então.')
				return
						
			
		elif int(user_input) == 4:
			print('Você escolheu excluir um de nossos cadastros, por favor indique o indice abaixo para que possamos excluir '
				  'o cadastro selecionado')
				  
			print('')	  
			show_cadastro(conn)
			print('')
			
			user_chose = int(input('Qual cadastro você deseja deletar? '))
			delete_cadastro(conn, user_chose)
			
			print('')
			print('Cadastro' +' '+str(user_chose)+' ' +' deletado com sucesso!')
			print('')
			
			show_cadastro(conn)
			print('')
			
			print('Deseja realizar mais alguma coisa? Sim(1), Não(2)')
			final_choice = int(input(''))
					
			if int(final_choice) == 1:
				print('')
				create_connection(user_path)

			elif int(final_choice) == 2:
				print('Tudo bem :) nos vemos em breve então.')
				return
					

		elif int(user_input) == 5:
			print('Estamos preparando tudo, daqui a alguns segundos vá ao seu diretório raiz que terá seu texto prontinho :)')
			query_text(conn)
			print('')

			print('Deseja realizar mais alguma coisa? Sim(1), Não(2)')
			final_choice = int(input(''))
					
			if int(final_choice) == 1:
				print('')
				create_connection(user_path)

			elif int(final_choice) == 2:
				print('Tudo bem :) nos vemos em breve então.')
				return
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close()

if __name__ == '__main__':
	create_connection(user_path)