from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this survey has super secret content'

@app.route('/')
def survey():

    return render_template("index.html")


# @app.route('/process')
# def save_submission():

#     return redirect("/")


# @app.route('/result')
# def confirmation():

#     return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)