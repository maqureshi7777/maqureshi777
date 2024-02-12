from flask import Flask , render_template , request
import joblib

model = joblib.load('Log_model.pkl')



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/career")
def func_1():
    return render_template('career.html')

@app.route("/Alumni")
def func_2():
    return "Alumni Page"

@app.route("/project")
def func_3():
    return "Welcome To project"

@app.route("/blog")
def func_4():
    return "Welcome To blog "


@app.route('/Login' , methods = ['post'])
def submit():
    a = request.form.get('user_name')
    b = request.form.get('ph_no')
    c = request.form.get('password')
    print(a , b , c)
    return 'Login Success'


@app.route('/Model' , methods = ['post'])
def model_pred():
    a = float(request.form.get('preg'))
    b = float(request.form.get('plas'))
    c = float(request.form.get('pres'))
    d = float(request.form.get('skin'))
    e = float(request.form.get('test'))
    f = float(request.form.get('pedi'))
    g = float(request.form.get('mass'))
    h = float(request.form.get('age'))
    re = model.predict([[a,b,c,d,e,f,g,h]])
    if re[0] ==1:
        return 'Person is diabetic'
    else:
        return 'Person is not diabetic'

app.run(debug= True)
