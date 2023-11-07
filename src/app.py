from flask import Flask, render_template, request, flash, redirect, url_for
import mysql.connector

app = Flask(__name__)


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='fatec',
    database='contacts'
)
app.config['SECRET_KEY'] = 'contatos'

cursor = conn.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("volei.html")

@app.route("/contacts", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
    
        cursor.execute('INSERT INTO contatos(con_email, con_assunto, con_desc) VALUES (%s, %s, %s)', (email, assunto, descricao))

        conn.commit()

        conn.close()
    
        flash('Mensagem Enviada!')
        return redirect(url_for('home'))

    return render_template("contacts.html")

@app.route("/usuarios")
def lista():
    usuarios = cursor.execute('SELECT * FROM contatos')
    usuarios = cursor.fetchall()
    
    return render_template('lista.html', usuarios=usuarios)

app.run(debug=True)
