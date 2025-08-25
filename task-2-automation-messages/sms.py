from twilio.rest import Client


account_sid = 'AC02f1eec79b392003d119597755ad'
auth_token = '69aa48e66ca855637c5bb2397a'


client = Client(account_sid, auth_token)


message = client.messages.create(
    to='+919709366834',  
    from_='+15203895896',  
    body='Hello, this is a test message!'
)

print(message.sid)
