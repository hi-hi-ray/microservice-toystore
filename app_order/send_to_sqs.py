import boto3


def send_to_sqs(id, id_toy, quantity):
    client = boto3.resource('sqs', region_name='sa-east-1',
                            aws_access_key_id="AKIAWJLET7HYQRUDAHFU",
                            aws_secret_access_key="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",
                            endpoint_url='https://sqs.sa-east-1.amazonaws.com/432392108529/ordertoystock')
    queue_name = 'ordertoystock'
    queue = client.get_queue_by_name(QueueName=queue_name)

    message = ("id: " + str(id) +
        " id_toy: "+  id_toy +
        " quantity: " + str(quantity))

    response = queue.send_message(MessageBody=message)
    print(response)
    if response.get('MessageId') != "":
        return "Success"
    else:
        return "Failed"
