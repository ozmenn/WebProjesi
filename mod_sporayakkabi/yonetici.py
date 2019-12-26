from app import app
from flask import render_template

@app.route('/spor')
def spor():
    spor=[ ]
    return render_template('sporayakkabi.html',title='Spor Ayakkabıları',veri=spor)