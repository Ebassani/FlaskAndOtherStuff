from math import sqrt

from flask import Flask, render_template, request, Response

from static.python.functions import *
from static.python.conn import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


'''
more than one page
'''


@app.route('/conn')
def con():
    conn = get_db_connection()
    conn.close()
    return 'hello'


@app.route('/create')
def create():
    create_table()
    return 'tables created'


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    return '''<h1>The name is {}</h1>'''.format(name)


@app.route('/sqrt')
def calc():
    def test():
        a = 9
        x = 1
        epsilon = 10 ** -10
        string = ''
        while True:
            string += str(x) + ","
            y = (x + a / x) / 2
            if abs(y - x) < epsilon:
                break
            x = y
        return string

    def values():
        value = ''
        for num1 in range(1, 500):
            for num2 in range(1, 500):
                if num1 ** 3 - num2 ** 2 == 100:
                    value += '(' + str(num1) + ',' + str(num2) + ')'
        return value

    def prime_num(num):
        for aux in range(2, int(sqrt(num)) + 1):
            if num % test == 0:
                return False
        return True

    def next_prime(num):
        num += 1
        while True:
            if prime_num(num):
                return num
            num += 1

    def is_palindrome(num):
        numstr = str(num)
        for i in range(int(len(numstr) / 2)):
            if numstr[i] != numstr[len(numstr) - i - 1]:
                return False
        return True

    def palindromes(num):
        pal = ''
        for i in range(1, num):
            if is_palindrome(i):
                pal += str(i) + ','
        return pal

    return test() + '<br>' + values() + '<br>' + str(prime_num(5)) + '<br>' + str(next_prime(14)) +\
        '<br>' + str(is_palindrome(42024)) + '<br>' + palindromes(300)
