# -*- coding: utf-8 -*-

from bottle import run, route


@route('/hello/<name>')
def index(name):
    return ('hello %s' % (name))


run(host='localhost', port=8080)