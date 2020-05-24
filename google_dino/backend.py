from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 

app=Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "Database.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class wheel2(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	vehicleno = db.Column(db.String(120), nullable = False)
	vehiclemodel = db.Column(db.String(80), nullable=False)
	name = db.Column(db.String(120), nullable=False)
	phoneno = db.Column(db.Integer, nullable=False)
	arrival = db.Column(db.String(100), nullable=False)
	departure = db.Column(db.String(100), nullable=True)

class wheel4(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	vehicleno = db.Column(db.String(120), nullable = False)
	vehiclemodel = db.Column(db.String(80), nullable=False)
	name = db.Column(db.String(120), nullable=False)
	phoneno = db.Column(db.Integer, nullable=False)
	arrival = db.Column(db.String(100), nullable=False)
	departure = db.Column(db.String(100), nullable=True)


@app.route('/')
@app.route('/home.html')
def root():
	return render_template('home.html')

@app.route('/2_wheeler.html')
def wheeler_2():
	return render_template('2_wheeler.html')

@app.route('/4_wheeler.html')
def wheeler_4():
	return render_template('4_wheeler.html')



if __name__ == '__main__' :
	app.run(debug = True)