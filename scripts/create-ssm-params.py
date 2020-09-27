import sys
import json
import boto3

with open('./values.json') as f:
  parameters = json.load(f)

client = boto3.client('ssm')

for param in parameters:
    try:
        response = client.put_parameter(
            Name=param['key'].replace('ENVIRONMENT', sys.argv[1]),
            Value=param['value'],
            Type='SecureString',
            KeyId='alias/Omni-DW-dev-kms',
            Overwrite=True
        )
    except Exception as e:
        print ("create parameter error: ", e)
        raise e
    
    try:
        response = client.add_tags_to_resource(
            ResourceType='Parameter',
            ResourceId=param['key'].replace('ENVIRONMENT', sys.argv[1]),
            Tags=[
                {
                    'Key': 'Application',
                    'Value': 'DataWarehouse'
                },
                {
                    'Key': 'CreateBy',
                    'Value': 'BizCloudExperts'
                },
                {
                    'Key': 'Environment',
                    'Value': sys.argv[1]
                },
                {
                    'Key': 'Version',
                    'Value': '1.0'
                }
            ]
        )
    except Exception as e:
        print ("add tags to parameter error: ", e)
        raise e

print ('params created successfully')