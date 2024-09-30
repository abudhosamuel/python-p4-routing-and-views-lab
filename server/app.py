#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route to display the title
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# View to print a string and display it
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # This prints the string to the console
    return f"{parameter}"

# View to count up to the provided number
@app.route('/count/<int:parameter>')
def count(parameter):
    return "\n".join([str(i) for i in range(parameter)])

# View to perform basic math operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    return f"{result}"

# Run the app
if __name__ == '__main__':
    app.run(port=5551, debug=True)
