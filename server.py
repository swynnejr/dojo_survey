from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this survey has super secret content'

@app.route('/')
def survey():
    return render_template("index.html")


@app.route('/process', methods = ['POST'])
def confirmation():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')


@app.route('/result')
def save_submission():

    return render_template('result.html', name = session['name'], location = session['location'], language = session['language'], comment = session['comments'])




if __name__ == "__main__":
    app.run(debug=True)