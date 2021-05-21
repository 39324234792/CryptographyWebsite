from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/Puzzle1')
def login():
    return render_template('puzzle1+.html')


@auth.route('/Puzzle1a')
def Answer1():
    return render_template('Answer1.html')


@auth.route('/Puzzle2')
def Puzzle2():
    return render_template('puzzle2+.html')


@auth.route('/Puzzle2a')
def Answer2():
    return render_template('Answer2.html')


@auth.route('/Puzzle3')
def Puzzle3():
    return render_template('puzzle3+.html')


@auth.route('/Puzzle3a')
def Answer3():
    return render_template('Answer3.html')


@auth.route('/in')
def instrucions():
    return render_template('instrustions.html')


@auth.route('/levels')
def levels():
    return render_template('Levels.html')
