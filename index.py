import json
import datetime

def calcular(n):
    n += 10
    return n

def handler(event, context):
    #data = {
    #    'output': 'Hello World',
    #    'timestamp': datetime.datetime.utcnow().isoformat()
    #}
    n = 1000
    data = calcular(n)
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

