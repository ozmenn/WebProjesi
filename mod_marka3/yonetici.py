#rotalar ve fonksiyon konacak

from app import app
from flask import render_template

@app.route('/marka3')
def marka3():
    marka3=[ ]
    return render_template('marka3.html',title='Spor Ayakkabıları',veri=marka3)