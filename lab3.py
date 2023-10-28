from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    age = request.args.get('age')
    sex = request.args.get('sex')
    if user == '':
        errors['user'] = 'Заполните поле!'
    if age == '':
        errors['age'] = 'Заполните поле!'
        user = ''
        errors['user'] = 'Заполните поле!'
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else: 
        price = 70


    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price +=10

    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    full_name = request.args.get('full_name')
    age = request.args.get('age')
    ticket_type = request.args.get('ticket_type')
    bunk = request.args.get('bunk')
    luggage = request.args.get('luggage')
    departure_point = request.args.get('departure_point')
    destination = request.args.get('destination')
    travel_date = request.args.get('travel_date')
    return render_template("ticket.html", full_name=full_name, age=age, ticket_type=ticket_type, bunk=bunk,luggage=luggage,departure_point=departure_point,
                           destination=destination,travel_date=travel_date)