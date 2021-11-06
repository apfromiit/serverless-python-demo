import json

def serverless(api):
    def function(event, context):
        body = api(event, context)
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response
    return function

@serverless
def hello1(event, context):
    params = event['queryStringParameters']
    if not params:
        params = {}
    name = params.get("name", "world")
    return { "hello": name }

@serverless
def hello2(event, context):
    params = event['pathParameters']
    return { "hello": params["name"] }

@serverless
def hello3(event, context):
    data = json.loads(event['body'])
    return { "hello": data.get('name', 'world') }