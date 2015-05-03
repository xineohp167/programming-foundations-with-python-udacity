from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACa17fcef62494018c0d73a23d89a74054"
auth_token  = "40d0b0dfd4e33b4aa9b5f9991dee1652"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="What's up?",
    to="+3590886023622",    # Replace with your phone number
    from_="+12403293233") # Replace with your Twilio number
print message.sid
