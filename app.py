from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hrView')
def company():
    return render_template('company.html')

@app.route('/tpoView')
def TPO():
    return render_template('tpo.html')

@app.route('/studentView')
def student():
    return render_template('student.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)