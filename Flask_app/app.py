from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('qq.html')

@app.route('/aa')
def aa():
    return render_template('aa.html')

if __name__ == '__main__':
    app.run(debug=True)
