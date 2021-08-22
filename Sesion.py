from flask import Flask, render_template, request, json, url_for, redirect,send_from_directory
from flaskext.mysql import MySQL
import os
import Modelo as Modelo
import requests
import json
import jinja2

app = Flask(__name__)

@app.errorhandler(404)

def not_found(e):
    return render_template("404.html")


@app.route("/") 
def index(): 
    return render_template("index.html")

@app.route("/QnA") 
def QnA(): 
    return render_template("FAQ.html")

@app.route("/catalogo") 
def catalogo(): 
    data=Modelo.catalogo()
    print(data)
    return render_template('catalogo.html',data=data)

@app.route("/contacto") 
def contacto(): 
    return render_template("contact.html")   
    

 

if __name__ == "__main__": 

    app.run() 