#rotalar ve fonksiyon konacak

from app import app
from flask import render_template

@app.route('/marka2')
def marka2():
    marka2=[ ]
    return render_template('marka2.html',title='Spor Ayakkabıları',veri=marka2)