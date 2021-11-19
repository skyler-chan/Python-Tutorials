import pywhatkit

phone_number = input(
    "Please input the phone number you wish to send automated messages to ")
message = input("Write your message ")
hour = int(input("Hour to be sent (24 hour) "))
minute = int(input("Minute to be sent "))
pywhatkit.sendwhatmsg(phone_number, message, hour, minute, 30, False, 3)
