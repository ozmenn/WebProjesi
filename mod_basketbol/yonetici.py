#rotalar ve fonksiyon konacak

from app import app
from flask import render_template

@app.route('/basketbol')
def basketbol():
    basketbol=[ ]
    return render_template('basketbol.html',title='Spor Ayakkabıları',veri=basketbol)