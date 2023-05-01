from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    msg = ''
    if request.method == 'POST':
        msg = "post worked well"
        first = request.form['first_number']
        second = request.form['second_number']
        third = request.form['third_number']
        sum = int(first) + int(second) + int(third)
        return render_template('home.html', ans=sum, msg=msg)
    msg = "post not worked"
        
    return render_template("home.html",msg=msg)


# @app.route('/index', methods=['POST'])
# def index():
#     msg = ''
#     if request.method == 'POST':
#         msg = "post worked well"
#         first = request.form['first_number']
#         second = request.form['second_number']
#         third = request.form['third_number']
#         sum = int(first) + int(second) + int(third)
#         return render_template('index.html', ans=sum, msg=msg)
#     msg = "post not worked"
        
#     return render_template("index.html",msg=msg)



app.run(debug=True, port=8000, host='0.0.0.0')