from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash

lab5 = Blueprint('lab5', __name__)

def dbConnect():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base',
        user = 'admin_knowledge_base',
        password = '123')    
    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route('/lab5/')
def lab():
    username = session.get('username')

    return render_template('databaselab5.html', username=username)


@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database='knowledge_base',
        user = 'admin_knowledge_base',
        password = '123')
    cur = conn.cursor()

    cur.execute('SELECT * FROM public.users;')

    users = cur.fetchall()

    cur.close()
    conn.close()
    user0 = users[0][1]
    user1 = users[1][1]
    user2 = users[2][1]
    user3 = users[3][1]
    return render_template("users.html", user0=user0, user1=user1, user2=user2, user3=user3)



@lab5.route('/lab5/registration', methods = ['GET', 'POST'])
def registation():

    errors = []

    if request.method == "GET":
        return render_template('register.html', errors=errors)
     
    username = request.form.get("username")
    password = request.form.get("password")


    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if username == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    if password == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT username FROM users WHERE username = %s;", (username,))

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")

        conn.close()
        cur.close()
        return render_template('register.html', errors=errors)
    
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    
    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/login5")

@lab5.route('/lab5/login5', methods=["GET", "POST"])
def login5():
    errors = []

    if request.method == "GET":
        return render_template("login5.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста заполните все поля")
        return render_template("login5.html", errors=errors)
    if username == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login5.html', errors=errors)
    if password == '':
        errors.append("Пожалуйста заполните все поля")
        print(errors)
        return render_template('login5.html', errors=errors)
    
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute("SELECT id, password FROM users WHERE username = %s;", (username,))

    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("login5.html", errors=errors)
    
    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5/")
    
    else:
        errors.append('Неправильный логин пароль')
        return render_template('login5.html', errors=errors)
