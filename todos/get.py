import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


## aaaaa jjjjjjjjj
### iiuiuiuiuiu
### ahora si?
##insisto




def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database hecho...
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response crearfffffff
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response
