from django.shortcuts import render
from django.http import HttpResponse

import pprint
from pymongo import MongoClient

def index(request):
    return HttpResponse("Bem indo ao RHTech.")

def index(request):
    client = MongoClient('mongodb+srv://mongo:mongo@aulasenai.kwftl.mongodb.net/?retryWrites=true&w=majority')
    
    db = client.rhtech
    print('db', db)
    print(db.list_collection_names())
    
    pontos = db.ponto
    
    pprint.pprint(pontos.find_one())
