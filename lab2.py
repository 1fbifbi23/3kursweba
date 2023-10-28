from flask import Blueprint, redirect, url_for, render_template, Blueprint, request

lab2 = Blueprint('lab2', __name__)



@lab2.route('/lab2/example')
def example():
    name = 'Ларионов Даниил Сергеевич'
    course = '2 курс'
    group = 'ФБИ-12'
    number_laboratory = '2'
    fruits = [
        {'name': 'Яблоки', 'price': 100},
        {'name': 'Груши', 'price': 166},
        {'name': 'Апельсины', 'price': 320},
        {'name': 'Бананы', 'price': 1030},
        {'name': 'Манго', 'price': 1520}
        ]
    
    books = [
        {'name': 'Куджо', 'author': 'Стивен Кинг', 'size': '400 страниц'},
        {'name': 'Мастер и Маргарита', 'author': 'Михаил Булгаков', 'size': '350 страниц'},
        {'name': '1984', 'author': 'Джордж Оруэлл', 'size': '328 страниц'},
        {'name': 'Война и мир', 'author': 'Лев Толстой', 'size': '1225 страниц'},
        {'name': 'Анна Каренина', 'author': 'Лев Толстой', 'size': '864 страницы'},
        {'name': 'Гарри Поттер и философский камень', 'author': 'Джоан Роулинг', 'size': '223 страницы'},
        {'name': 'Маленький принц', 'author': 'Антуан де Сент-Экзюпери', 'size': '96 страниц'},
        {'name': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'size': '480 страниц'},
        {'name': 'Алхимик', 'author': 'Пауло Коэльо', 'size': '208 страниц'},
        {'name': 'Метро 2033', 'author': 'Дмитрий Глуховский', 'size': '416 страниц'}
        ]
    return render_template('example.html', name=name, course=course, group=group, number_laboratory=number_laboratory, fruits=fruits, books=books)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/language')
def language():
    return render_template('language.html')