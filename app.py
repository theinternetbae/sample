from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12241468'
app.config['MYSQL_PASSWORD'] = 'TqlYbhCr2Z'
app.config['MYSQL_DB'] = 'sql12241468'

mysql = MySQL(app)


@app.route('/')
def index():
    title = "Farhan"
    return render_template('index.html', title=title)

@app.route('/imgprocessing')
def imgprocessing():
    title = 'improcessing'
    return render_template('imgprocessing.html', title=title)

@app.route('/paru')
def paru():
    title = 'paru'
    return render_template('paru.html', title=title)

@app.route('/crud')
def crud():
    title = 'crud'
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('crud.html', students = data, title=title)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        flash("Data Inserted Successfully")

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('crud'))

@app.route('/update', methods = ['POST', 'GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE students SET name=%s, email=%s, phone=%s WHERE no=%s", (name, email, phone, id_data))
        flash("Data updated successfully")
        mysql.connection.commit()
        return redirect(url_for('crud'))
    else:
        flash("Failed")

@app.route('/delete/<string:id_data>', methods = ['POST', 'GET'])
def delete(id_data):

    flash('Data deleted successfully')

    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM students WHERE no = %s', (id_data))
    mysql.connection.commit()
    return redirect(url_for('crud'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)