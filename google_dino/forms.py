from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class VehicleForm(FlaskForm):
	numberplate=StringField('Vehicle No.')
	model=StringField('Vehicle Model',validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
	name=StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
	phone=StringField('Phone', validators=[Length(min=-1, max=20, message='You cannot have more than 20 characters')])
	arrival=StringField('Arrival')
	dep=StringField('Departure')