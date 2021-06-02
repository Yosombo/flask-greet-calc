from flask import Flask, request
import operations
app = Flask(__name__)


@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = str(operations.add(a, b))
    return res


@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = str(operations.sub(a, b))
    return res


@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = str(operations.mult(a, b))
    return res


@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = str(operations.div(a, b))
    return res


math_operations = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}


@app.route('/math/<oper>')
def math(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = math_operations[oper](a, b)

    return str(res)
