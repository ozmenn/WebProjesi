from flask import Flask

app = Flask(__name__)

import mod_anasayfa.yonetici

import mod_sporayakkabi.yonetici
import mod_marka1.yonetici
import mod_basketbol.yonetici
import mod_voleybol.yonetici
import mod_marka2.yonetici
import mod_futbol.yonetici
import mod_marka3.yonetici







if __name__ == '__main__':
    app.run()
