from flask import Flask, render_template, request
from waitress import serve
from calculate import calculator

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/calculate")
def operation():
    num1 = request.args.get("num1")
    operation_symbol = request.args.get("operation_symbol")
    num2 = request.args.get("num2")

    input1 = float(num1)
    input2 = float(num2)

    if operation_symbol == "+":
        answer = input1 + input2
    elif operation_symbol =="-":
        answer = input1 - input2
    elif operation_symbol == "*":
        answer = input1 * input2
    try:
        if operation_symbol == "/":
            answer = input1 / input2
    except ZeroDivisionError:
        return render_template("invalid-number.html")

    if operation_symbol != "+" and operation_symbol != "-" and operation_symbol != "*" and operation_symbol != "/":
        return render_template("invalid-input.html")

    return render_template(
        "calculate.html",
        num1 = input1,
        operation_symbol = operation_symbol,
        num2 = input2,
        answer = answer
    )

if __name__ == "__main__":
   serve(app, host="0.0.0.0", port=9000)