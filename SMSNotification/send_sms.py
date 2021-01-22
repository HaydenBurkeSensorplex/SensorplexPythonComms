'''
Basic sms notification service for sms using Twilio a paid subscription service
Conducted on trail account

Website: https://www.twilio.com/
Documentation: https://www.twilio.com/docs/libraries/python
'''

from twilio.rest import Client

#This two varibles must be kept hidden, see documentation of how to secure them.
account = "ACc9b51b895ccd118e28bab254af83ab89"
token = "6dbeceb5e172897f6011d24c494bb9eb"

client = Client(account, token)

message = client.messages.create(to='+61432855949',from_='+19178314961', body='Hello World')

print(message.sid)