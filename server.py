from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 0
    if 'visits' not in session:
        session['visits'] = 1
    else:
        session['visits'] += 1
    return render_template('check.html')

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')

@app.route('/', methods = ['POST'])
def increment_by_two():
    if 'plus_two_btn' in request.form:
        session['count'] += int(request.form['number'])
    if 'clear_btn' in request.form:
        # session.clear()		# clears all keys
        session.pop('count')		# clears a specific key

    return redirect('/')
        

if __name__ == '__main__':
    app.run(debug = True)
