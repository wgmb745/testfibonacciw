import json
import datetime


def handler(event, context):
    """
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    """
    data = calcular(numero)
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}

def calcular(self,n):
    return n
