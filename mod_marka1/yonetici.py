from app import app
from flask import render_template

@app.route('/marka1')
def marka1():
    marka1=[ ]
    return render_template('marka1.html',title='Spor Ayakkabıları',veri=marka1)