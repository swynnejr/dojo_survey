from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this survey has super secret content'







if __name__ == "__main__":
    app.run(debug=True)