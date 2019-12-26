#rotalar ve fonksiyon konacak

from app import app
from flask import render_template

@app.route('/')
def blogMesajlari():
    mesajlar=[ ]
    return render_template('anasayfa.html',title='Spor Ayakkabıları',veri=mesajlar)

@app.route('/anasayfa')
def anasayfa():
    anasayfa=[ ]
    return render_template('anasayfa.html',title='Spor Ayakkabıları',veri=anasayfa)