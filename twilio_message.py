from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC90e4381fec59531e4676b66b8a9a087f"
# Your Auth Token from twilio.com/console
auth_token  = "1877f5dd5e887575ee665f076192a4bc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12134667020",
    from_="+18564463740",
    body="Hello from Python!")

print(message.sid)