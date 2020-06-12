import json
import datetime

def handler(event, context):
    #lista = []
    #for i in event:
    #    lista.append(i)
    data = {
        'output': 'Hello World',
        'prueba', 'Test1'
        'lista': event,
        'prueba2', 'Test2'
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
