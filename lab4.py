from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    username = request.form.get('username')
    password = request.form.get('password')
    error = None 
    if not username and not password:
        error = 'Нет логина и пароля'
    elif not username:
        error = 'Нет логина'
    elif not password:
        error = 'Нет пароля'
    elif username == 'alex' and password == '123':
        return render_template("success_lab4.html", username=username)
    else:
        error = 'Неверный логин или пароль!'

    return render_template("login.html", error=error, username=username, password=password)


@lab4.route('/lab4/freeze/', methods=['GET', 'POST'])
def freeze():
    if request.method == 'GET':
        return render_template("freeze.html")

    temperature = request.form.get('temperature')
    message = None
    if not temperature:
        message = 'Не задана температура'
    elif int(temperature) < -12:
        message = 'Не удалось установить температуру слишком низкое значение'
    elif int(temperature) > -1: 
        message = 'Не удалось установить температуру слишком высокое значение'
    elif int(temperature) >=-12 and int(temperature) <=-9:
        message = f"Установлена температура {temperature} ***"
    elif int(temperature) >=-8 and int(temperature) <=-5:
        message = f"Установлена температура {temperature} **"
    elif int(temperature) >=-4 and int(temperature) <=-1:
        message = f"Установлена температура {temperature} *"     

    return render_template('freeze.html', temperature=temperature, message=message)


@lab4.route('/lab4/zerno/', methods=['GET', 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template("zerno.html")

    zerno = request.form.get('zerno')
    zerno_weight = request.form.get('zerno_weight')
    message = None
    price = 0


    if zerno == 'Ячмень':
        price = 12000
    elif zerno == 'Овес':
        price = 8500
    elif zerno == 'Пшеница':
        price = 8700
    elif zerno == 'Рожь':
        price = 14000
    else:
        price = 0

    sum = price * float(zerno_weight)
    discount = None
    if not zerno_weight:
         message = 'Некорректный вес'

    if float(zerno_weight) >= 50 and float(zerno_weight) <=499:
        sum = (price * float(zerno_weight)) * 0.9
        discount = (price * float(zerno_weight)) * 0.1 
        message = f'За взятый объем свыше 50 тонн присовена скидка = {discount} руб. Финальная цена товара составит = {sum}руб.'
    if float(zerno_weight) <= 50:
        message = f'Цена товаров = {sum}руб.'
    if float(zerno_weight) >= 500:
        message = 'Такого обьема зерна нет в наличии'
    if zerno_weight == '':
        message = 'Невведен вес'
    if float(zerno_weight) <= 0:
        message = 'Неккоректное значение веса'

    return render_template('zerno.html', zerno=zerno, zerno_weight=zerno_weight, message=message, price=price)    


@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template("cookies.html")
    color = request.form.get('color')
    background_color = request.form.get('background_color')
    font_size = request.form.get('font_size')
    message = None

    if color == background_color:
        message = 'Цвет текста совпадает с фоном'
        return render_template("cookies.html", message=message)

    headers = {
        'Set-Cookie': ['color=' + color + '; path=/',
                       'background_color=' + background_color + '; path=/',
                       'font_size=' + str(font_size) + '; path=/'],
        'Location': '/lab4/cookies'
    }
    return '', 303, headers

