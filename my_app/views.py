#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.models import Url
import time
import serial
import os
from bs4 import BeautifulSoup
import requests

          
url = Blueprint('url', __name__) 
@url.route('/')
@url.route('/home')

def home():
    return "Welcome to the Catalog Home."
 
 
class UrlView(MethodView):
 
    def get(self, id=None, page=1):   
        arquivo = open('url.txt', 'r')
        conteudo = arquivo.readlines()
        print conteudo
        
        return jsonify({"url" : conteudo})  
 
    def post(self):       
        url_string = request.form.get('url')        
        path = "./"
        dir = os.listdir(path)
        for file in dir:
            if file == "url.txt":
                os.remove(file)
        
        conteudo = 'suelliton'

        # Abre novamente o arquivo (escrita)
        # e escreva o contedo criado anteriormente nele.
        arquivo = open('url.txt', 'w')

        arquivo.write(url_string)
        arquivo.close()
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
url_view =  UrlView.as_view('url_view')
app.add_url_rule(
    '/url/', view_func=url_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/url/<int:id>', view_func=url_view, methods=['GET']
)

        