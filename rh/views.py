from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse

import redis
import pprint
from pymongo import MongoClient

def index(request):
    return render(request, 'index.html')

def registro_mongo(request):
        
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        try:
            ponto = {
                "colaborador" : {
                    "id" : 25.0, 
                    "nome" : "Tiago Lopes", 
                    "idade" : 32.0, 
                    "cargo" : {
                        "id" : 33.0, 
                        "cargo" : "Analista", 
                        "departamento" : "Suporte Tecnico"
                    }
                }, 
                "data" : datetime.now().strftime("%d-%m-%Y"), 
                "ponto" : [
                    {
                        "tipo" : "entrada", 
                        "hora" : "08:10:49.689"
                    }, 
                    {
                        "tipo" : "saida", 
                        "hora" : "12:15:49.689"
                    }, 

                ], 
                "jornada" : 8.75  
            }
  
            client = MongoClient('mongodb+srv://mongo:mongo@aulasenai.kwftl.mongodb.net/?retryWrites=true&w=majority')
    
            db = client.rhtech
            print('db', db)
            print(db.list_collection_names())

            pontos = db.folha_ponto
            ponto_id = pontos.insert_one(ponto).inserted_id
            ponto_id

        except:
            return JsonResponse({'response': 'Invalid request'}, status=400)
        
    else:
        return JsonResponse({'response': 'Invalid request'}, status=400)
    
    return JsonResponse({'response': f'Ponto {ponto_id} registrado com sucesso'}, )


def ponto_redis(request):
    print(request)
    
    try:    
        r = redis.Redis(
            host='redis-10782.c10.us-east-1-2.ec2.cloud.redislabs.com',
            port=10782, 
            password='Tx8rR5v7fguToeN7rowBSeit5IpppTrd')
        
        print('Registro Ponto no Redis', r)

        chave = f'Mateus-{datetime.now().strftime("%d-%m-%Y")}'
        print(chave)
        r.set(chave, str(datetime.now()))
        
        value = r.get(chave)
        print(value)
            
    except:
        return JsonResponse({'response': 'Invalid request'}, status=400)
        
    
    return JsonResponse({'response': f'ponto {chave} : {value}'}, )