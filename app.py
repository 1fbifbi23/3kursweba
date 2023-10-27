from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def start():
    return redirect('/menu', code=302)

@app.route('/menu')
def menu():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <a href='/lab1'>Лабораторная 1</a>
        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route('/lab1')
def lab1():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Даниил Ларионов, Лабораторная 1</title>
    </head>
    <body>
        <header>
            Нгту, ФБ, Лабораторная 1
        </header>
        <h1>WEB-сервер на flask</h1>
        <div>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые ба-
            зовые возможности.
        </div>
        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route('/oak')
def oak():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Даниил Ларионов, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1 id='oak'>OAK</h1>
        <div id='oak_image'>
            <img src="''' + url_for('static', filename='oak.jpg') + '''">
        </div>
    </body>
</html>
'''
