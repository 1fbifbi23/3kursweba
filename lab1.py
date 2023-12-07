from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab1 = Blueprint('lab1', __name__)

@lab1.route('/')
@lab1.route('/index')
def start():
    return redirect('/menu', code=302)

@lab1.route('/menu')
def menu():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
          <div id='labs'> Лабораторные работы
            <li><a href='/lab1'>Лабораторная 1</a></li>
            <li><a href='/lab2/'>Лабораторная 2</a></li>
            <li><a href='/lab3/'>Лабораторная 3</a></li>
            <li><a href='/lab4/'>Лабораторная 4</a></li>
            <li><a href='/lab5/'>Лабораторная 5</a></li>
            <li><a href='/lab6/'>Лабораторная 6</a></li>
            <li><a href='/lab7/'>Лабораторная 7</a></li>
        </div>
        <div id='rout'>
            <h1>Реализованные Роуты</h1>
            <ol>
                <li><a href='/oak'>Dub</a></li>
                <li><a href='/lab1/student'>Student</a></li>
                <li><a href='/lab1/python'>Python</a></li>
                <li><a href='/lab1/choice'>Choice</a></li>
            </ol>
        </div>
                
        <footer>
            &copy; Даниил Ларионов, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@lab1.route('/lab1')
def lab():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
'''

@lab1.route('/oak')
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

@lab1.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Ларионов Даниил Сергеевич, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>НГТУ</h1>
        <div>Ларионов Даниил Сергеевич</div>
        <img id='ngtu' src="''' + url_for('static', filename='ngtu.png') + '''">
    </body>
</html>
'''

@lab1.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Ларионов Даниил Сергеевич, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div id='python'>
            Python (МФА: [ˈpʌɪθ(ə)n]; в русском языке встречаются названия пито́н[23] или па́йтон[24]) — 
            высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[25][26], 
            ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём 
            программ[27]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. Необычной особенностью языка является выделение 
            блоков кода пробельными отступами[28]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[27]. 
            Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[25]. Недостатками языка являются зачастую более низкая скорость работы и 
            более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[25][27].
        </div>
        <img id='python_image' src="''' + url_for('static', filename='python.jpeg') + '''">
    </body>
</html>
'''

@lab1.route('/lab1/choice')
def choice():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <title>Ларионов Даниил Сергеевич, Лабораторная 1</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <div id='kit'>
            Как и все млекопитающие, киты дышат воздухом при помощи лёгких, являются теплокровными, кормят детёнышей молоком из молочных желёз и обладают волосяным покровом (хотя и довольно редуцированным)[9].
            Тело веретенообразное, наподобие обтекаемого тела рыб. Плавники, иногда также называемые ластами, имеют лопастеообразный вид. На конце хвоста расположен плавник из двух горизонтальных лопастей, играющий роль двигателя и стабилизатора, 
            обеспечивая движение вперёд благодаря волнообразным движениям в вертикальной плоскости (в отличие, например, от рыб и водных пресмыкающихся, 
            у которых плоскость движения гребного хвоста горизонтальна).
            Для защиты кожи от пагубного действия ультрафиолетовых лучей Солнца у разных групп китообразных выработаны разные защитные приспособления: одни, например синий кит, способны увеличивать содержание в коже поглощающих ультрафиолет пигментов («загорать»); другие, как кашалот, запускают особый «стрессовый ответ», как для защиты от кислородных радикалов; третьи, как финвал, используют оба способа[10]. 
            В холодной воде киты поддерживают температуру своего тела благодаря толстому слою жира под кожей. Этот слой защищает внутренние органы от переохлаждения.
            Из-за того что китам, как и дельфинам, необходимо изредка подниматься на поверхность для дыхания, только половина их мозга может спать в определённый момент времени.
        </div>
        <img id='kit_image' src="''' + url_for('static', filename='kit.jpg') + '''">
    </body>
</html>
'''