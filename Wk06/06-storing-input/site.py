from flask import Flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'important to keep unknown in production'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired




class MyForm(Form):
    """A class definition for a form object.

    Attributes: 
        first_name (object)
        last_name (object)
    """
    first_name = StringField('First name:', validators=[DataRequired()])
    last_name = StringField('Last name:', validators=[DataRequired()])
    # Fields are responsible for rendering and data conversion
    # They delegate to optional validators for data validation
    # StringField is the base for most of the more complicated fields, 
    # and it represents <input type="text">
    # DataRequired checks that the data attribute on the field is a ‘true’ value
    

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)  # create database
db.create_all()  # create all tables (will not recreate tables already present in database)


class Visitor(db.Model):
    """A class definition for a visitor MetaData object. 
    
    Attributes (initalized in __init__):
        first_name (string)
        last_name (string)

    """
    # create columns for database table (not yet set)
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    

    def __repr__(self):
        return '<Visitor {0}, {1}>'.format(self.first_name, self.last_name)
    

@app.route('/', methods=('GET', 'POST'))
def index():
    """Process form for each visitor and return rendered HTML."""

    form = MyForm()
    previous_visitors = Visitor.query.order_by('id DESC').all()

    # check if form submission is a valid POST request
    if form.validate_on_submit():
        first_name = form.first_name.data  # retrieve first name from form
        last_name = form.last_name.data  # retrieve last name from form
        db.session.add(Visitor(first_name, last_name))  # set columns in database table
        db.session.commit()  # write changes to the database
    else:
        first_name = 'stranger'
        last_name = None

    return render_template('index.html', form=form, first_name=first_name, last_name=last_name, previous_visitors=previous_visitors)
    
    
if __name__ == '__main__':
    app.run(debug=True)
