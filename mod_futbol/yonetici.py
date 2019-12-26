#rotalar ve fonksiyon konacak

from app import app
from flask import render_template

@app.route('/futbol')
def futbol():
    futbol=[ ]
    return render_template('futbol.html',title='Spor Ayakkabıları',veri=futbol)