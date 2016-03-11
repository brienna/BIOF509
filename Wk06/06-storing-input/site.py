from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'important to keep unknown in production'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired




class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
    

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


    def __init__(self, name):
        self.name = name
    

    def __repr__(self):
        return '<Visitor %r>' % self.name
    
    
db.create_all()
    
@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    previous_visitors = Visitor.query.order_by('id DESC').all()
    if form.validate_on_submit():
        name = form.name.data
        db.session.add(Visitor(name))
        db.session.commit()
    else:
        name = 'stranger'
    return render_template('index.html', form=form, name=name, previous_visitors=previous_visitors)
    
@app.route('/custom/<custom>/')
def custom(custom):
    return render_template('custom.html', custom=custom)
    
if __name__ == '__main__':
    app.run(debug=True)
