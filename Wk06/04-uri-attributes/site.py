from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/custom/<custom>/')
def custom(custom):
    return render_template('custom.html', custom=custom)
    
if __name__ == '__main__':
    app.run(debug=True)
