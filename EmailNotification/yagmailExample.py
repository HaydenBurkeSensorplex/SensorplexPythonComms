'''
This code uses the ease-of-use library yagmail to more easily and rapidly structure script for sending emails

Documentation: https://blog.mailtrap.io/yagmail-tutorial/
'''

import yagmail

receiver = "hayden@sensorplex.com"
body = "Hello there from Yagmail"


yag = yagmail.SMTP("sensorplexnotification@gmail.com", "Goodman88!")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body
)