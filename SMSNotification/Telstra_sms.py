'''
Telstra API for SMS notifications

Untested 
'''

from __future__ import print_function
import time
import Telstra_Messaging
from Telstra_Messaging.rest import ApiException
from Telstra_Messaging import Configuration
from pprint import pprint
import urllib3

# Defining host is optional and default to https://tapi.telstra.com/v2
configuration = Configuration("https://tapi.telstra.com/v2")
x = Telstra_Messaging.ApiClient(configuration)
# Create an instance of the API class
api_instance = Telstra_Messaging.AuthenticationApi(x)
client_id = 'client_id_example' # str | 
client_secret = 'client_secret_example' # str | 
grant_type = 'client_credentials' # str |  (default to 'client_credentials')
scope = 'scope_example' # str | NSMS (optional)

try:
    # Generate OAuth2 token
    api_response = api_instance.auth_token(client_id, client_secret, grant_type, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_token: %s\n" % e)

