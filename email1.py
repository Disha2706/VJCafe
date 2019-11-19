
import smtplib

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("dishacheck123@gmail.com", "2rasika4")

#Send the mail
msg = "SENT FROM PYTHON3.7" # The /n separates the message from the headers
server.sendmail("dishacheck123@gmail.com", "ayushrl2005@gmail.com", msg)