import json
import datetime

def handler(event, context):
    if event is not None:
        num = 1
    data = {
        'output': 'Hello World',
        'prueba': 'Test1'
        'prueba2': 'Test2'
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
