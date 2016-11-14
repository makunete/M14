# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)

from random import randint


n = randint(1,100)
# el decorator (@) estableix la ruta (URL). A mes, activem el mètode POST
@app.route("/checknum", methods=["GET","POST"])

def checknum():
    global n
    # inicialitzem missatge
    miss = "No has enviat cap numero encara per comprovar."
    if request.method == "POST":
        # si entrem aquí és que ja hem enviat alguna dada del formulari (POST)
        numero = request.form["numero"]
        numero = int(numero)
        # quan posem accents cal avisar que és un string unicode amb la "u" a davant 
        # busquem que el email contingui al menys una @ i un .
        
        
        if numero < n:
            miss = "El numero es mes gran"
        elif numero > n:
            miss = "El numero es mes petit"
        elif numero==n:
            miss = "El numero es correcte"
            n = randint(1,100)


    # renderitzem el template amb el missatge pertinent
    return render_template( "checknum.html", missatge=miss )
 
if __name__ == "__main__":
    app.run()