from app import app
from flask import render_template

@app.route('/voleybol')
def voleybol():
    voleybol=[ ]
    return render_template('voleybol.html',title='Spor Ayakkabıları',veri=voleybol)