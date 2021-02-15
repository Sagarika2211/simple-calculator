# calcweb

from flask import Flask, render_template, url_for, request, redirect
import math

app = Flask(__name__)               # create a new flask application

# define basic routes

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'GET':
        # render the add page
        return render_template("add.html")
    else:
        # read the values from the form
        n1 = int(request.form['n1'])   # read the value from the first number input
        n2 = int(request.form['n2'])  # read the value from the second number input

        return redirect(url_for("result", n1 = n1, n2 = n2, operation = 'add', answer = n1 + n2))

@app.route("/subtract", methods=['GET', 'POST'])
def subtract():
    if request.method == 'GET':
        # render the subtract method
        return render_template("subtract.html")
    else:
        # read and cast the values from the form
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])

        # subtract the values
        answer = n1 - n2

        # redirect the user to the result page
        return redirect(url_for("result", n1 = n1, n2= n2, operation = 'subtract',answer=answer))
        
@app.route("/multiply", methods=['GET', 'POST'])
def multiply():
    if request.method == 'GET':
        # render the subtract method
        return render_template("multiply.html")
    else:
        # read and cast the values from the form
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])

        # subtract the values
        answer = n1 * n2

        # redirect the user to the result page
        return redirect(url_for("result", n1 = n1, n2= n2, operation = 'multiply', answer=answer))

@app.route("/divide", methods=['GET', 'POST'])
def divide():
    if request.method == 'GET':
        # render the subtract method
        return render_template("divide.html")
    else:
        # read and cast the values from the form
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])


        # subtract the values
        answer = n1 / n2

        # redirect the user to the result page
        return redirect(url_for("result", n1 = n1, n2= n2,  operation = 'divide', answer=answer))

@app.route("/")
def index():
    my_menu = [
        {"title":"Add", "url":url_for('add')},
        {"title":"Subtract", "url":url_for('subtract')},
        {"title":"Multiply", "url":url_for('multiply')},
        {"title":"Divide", "url":url_for('divide')},
        {"title":"Cube", "url":url_for('cube')},
        {"title":"Square Root", "url":url_for('sqrt')},
        {"title":"Absolute", "url":url_for('absolute')},
        {"title":"Angle_sct", "url":url_for('angle_sct')}
    ]
    return render_template("index.html", menu = my_menu)

@app.route("/angle_sct" , methods=["GET","POST"])
def angle_sct ():
    if request.method == 'GET':
        # render the subtract method
        return render_template("angle_sct.html")
    else:
        # read and cast the values from the form
        n1 = float(request.form['n1'])
        rad = math.radians(n1)
        # angle_sct the value
                 
        # redirect the user to the result page
        return redirect(url_for("result", n1=0 ,n2=0 , sin_1= round(math.sin(rad),1), cos_1=round(math.cos(rad),1), tan_1=round(math.tan(rad),1) , operation = 'angle_sct',answer=0))
        
       
@app.route("/absolute" , methods=["GET","POST"])
def absolute ():
    if request.method == 'GET':
        # render the subtract method
        return render_template("absolute.html")
    else:
        # read and cast the values from the form
        n1 = int(request.form['n1'])
        
        # abs the value
        answer = abs(n1)
        # redirect the user to the result page
        return redirect(url_for("result", n1 = n1, n2 = 0, operation = 'absolute', answer=answer))


@app.route("/cube", methods=['GET', 'POST'])
def cube():
    if request.method == 'GET':
        # render the subtract method
        return render_template("cube.html")
    else:
        # read and cast the values from the form
        n1 = int(request.form['n1'])
        
        # subtract the values
        answer = n1 ** 3

        # redirect the user to the result page
        return redirect(url_for("result", n1 = n1, n2 = 0, operation = 'cube' ,answer=answer))

@app.route("/sqrt", methods=['GET', 'POST'])
def sqrt():
    if request.method == 'GET':
        # render the subtract method
        return render_template("sqrt.html")
    else:
        n1 = int(request.form['n1'])
        if n1 > 0 :
            answer = n1 ** (1/2)
            return redirect(url_for("result", n1 = n1, n2 = 0,  operation = 'sqrt',answer=answer))
        else:
            return "You should only enter a positive number"


@app.route("/result/<n1>/<n2>/<sin_1>/<cos_1>/<tan_1>/<operation>/<float:answer>")
@app.route("/result/<n1>/<n2>/<operation>/<int(signed=Ture):answer>")
def result(n1, n2,operation,answer=None,sin_1=None,cos_1=None,tan_1=None):
    return render_template("result.html", n1 = n1, n2 = n2,sin_1=sin_1,cos_1=cos_1,tan_1=tan_1, operation = operation, result=answer, go_home=url_for("index"))




# run your flask application

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)           # run the flask app
