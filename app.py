from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    return """
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <a>Лабораторная 1</a>
        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""