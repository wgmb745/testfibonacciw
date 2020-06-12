import json
import datetime

def calcular(n):
    return n

def handler(event, context):
    """
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    """
    data = calcular(1000)
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

