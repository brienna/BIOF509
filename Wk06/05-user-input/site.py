from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'important to keep unknown in production'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired




class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
	
	
@app.route('/', methods=('GET', 'POST'))
def index():
	form = MyForm()
	if form.validate_on_submit():
		name = form.name.data
	else:
		name = 'stranger'
	return render_template('index.html', form=form, name=name)
	
@app.route('/custom/<custom>/')
def custom(custom):
	return render_template('custom.html', custom=custom)
	
if __name__ == '__main__':
	app.run(debug=True)