from __future__ import print_function

import base64
import boto3
import json
import uuid

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
    table = dynamodb.Table('DEMO-Serverless-Pipeline-DynamoDB')
    sns = boto3.client('sns')

    for record in event['Records']:
       #Kinesis data is base64 encoded so decode here
       payload=base64.b64decode(record["kinesis"]["data"]).decode('utf-8')
       decoded_payload = json.loads(payload)
       output_record = {
            'testingId': str(uuid.uuid4()),
            'sensorId': decoded_payload['sensorId'],
            'currentTemperature': decoded_payload["currentTemperature"],
            'status': decoded_payload["status"],

        }

       print("Decoded payload: " + str(output_record))
       table.put_item(Item=output_record)
       
       if decoded_payload["status"] == "FAIL":
        response = sns.publish(
            TopicArn='arn:aws:sns:eu-central-1:779684591593:testing-stream-1',
            Message=json.dumps(output_record),
            )

    print("Function done.")