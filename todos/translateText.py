import os
import json




from todos import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    
def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database hecho...
    resultTB = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    
    result = translate.translate_text(Text="Hello, World",
                                  SourceLanguageCode="es",
                                  TargetLanguageCode="en")
                                  
                               
                                  
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                            cls=decimalencoder.DecimalEncoder)
    }
    
    
    return result
