import json

def hello1(event, context):
    params = event['queryStringParameters']
    if params == None:
        name = "world"
    else:
        name = params.get("name")
        if name == None:
            name = "world"
    body = {
        "hello": name,
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def hello2(event, context):
    params = event['pathParameters']
    body = {
        "hello": params["name"],
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def hello3(event, context):
    data = json.loads(event['body'])
    body = {
        "hello": data['name']
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response