from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder='.')

@app.route('/')
def root():
    return render_template('index2.html')


app.run(debug=True, port=4000)
