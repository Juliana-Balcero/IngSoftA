from flask import Flask , render_template
from flask import request
from flask_bootstrap import Bootstrap
import pymysql

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	
	return render_template('index.html')


connection = pymysql.connect(
host = "localhost", 
user = "root",
password = "1230",
db = "beadsapp")
	
cursor = connection.cursor()

def leer():
	sql = "SELECT name  FROM data3"

	cursor.execute(sql)

	for name in cursor.fetchall():
		n = ("{0}" .format(name))
	
	return n 


@app.route('/hola',methods=['GET', 'POST'])	
def hola():
	respuesta1 = request.args.get('nombre')
	
	sql = """INSERT INTO data3(name) VALUES (%s)"""
	recordTuple=(respuesta1)

	cursor.execute(sql,recordTuple)
	
	connection.commit()
	
	u= leer()
	
	return render_template('index.html', m = request.method , j = respuesta1 , k= u ) 


if __name__ == "__main__":
	app.run(debug=True)