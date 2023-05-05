# Example from the Docs  https://github.com/sendgrid/sendgrid-python
# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# # 
# from urllib.request import urlopen
# import re as r
 
# # api key
# api_key= "api_key"

# Get locally used IP on device e.g. localhost aka 127.0.0.1
# import socket
# hostname = socket.gethostname()
# IPAddr = socket.gethostbyname(hostname) 
# print("Your Computer Name is:" + hostname)
# print("Your Computer IP Address is:" + IPAddr)

# Run in subshell on Windows
# dct = {}
# def infoDevice():
#     from platform import platform, machine, system, processor, node
#     dct['os'] = {
#         "devices": platform()[:10],
#         'machines': machine(),
#         'processors': processor()[:5],
#         'nodes': node(),
#         'systems': system(),
#     }
#     return dct

# infoDevice()
# # print(dct['os']['systems'])

# # Run bash in Linux | before need to get intro to OS's that not yet used to get hands dirty. 
# # Than use engineering to get exact IP address as well change os module to subprocess module or javascript module
# def tst():
#     if dct['os']['systems'] == "Linux":
#         print(os.system('ip addr show eth0'))  
#     elif dct['os']['systems'] == "macOS":
#         # Better get intro with MacOS terminal than do your staff...
#         print(os.system('ip addr show eth0'))    
#     elif dct['os']['systems'] == "Windows":
#         get_wifi_adapter = os.system("ipconfig | findstr 'Wireless LAN adapter Wifi' ") # need to add loop Wireless than
#         # if get_wifi_adapter ......
#     # elif os.systems == ChromeOS:
#         print(os.system('ip addr'))
#     elif dct['os']['systems'] == "iOS":
#         # Better get an intro to iOS functionality 
#         print(os.system('ip addr show eth0'))
#     elif dct['os']['systems'] == "iPadOS":
#         # Better get an intro to iOS functionality 
#         print(os.system('ip addr show eth0'))
#     # elif os.systems == further os to detect 
#     else:
#         return "OS not detected."
#     return 
# print(tst())


# Get IP address using the url 
# def getIP():
#     """Whatever IP address locater website you use urllib does do the wonder for you"""
#     # Oracle hosted IP locater.
#     d = str(urlopen('http://checkip.dyndns.com/').read())
#     return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
#     # # Let's get ip addres from https://ipdata.co/
#     # columbianos = str(urlopen('http://checkip.dyndns.com/').read())
#     # return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
# print(getIP())

# JAVASCRIPT: node.js called from Python
# from javascript import require, globalThis
# chalk, fs = require("chalk"), require("fs")
# print("Hello", chalk.red("world!"), "it's", globalThis.Date().toLocaleString())
# fs.writeFileSync("HelloWorld.txt", "hi!")
#
# from javascript import require, On, off, Once, once
# time = require('./rm.js')
# print(time.whatTimeIsIt())
# 
# from javascript import AsyncTask, start, stop, abort
# @AsyncTask(start=True)
# def routine(task: TaskState):
#   while not task.stopping: # You can also just do `while True` as long as you use task.sleep and not time.sleep
#     ... do some repeated task ...
#     task.sleep(1) # Sleep for a bit to not block everything else
# start(routine)
# time.sleep(1)
# stop(routine)
# Not preferred, but it stops all trouble
# abort(fn, seconds)

# def send_emails(to_email, text):
#     message = Mail(
#         from_email='your_email_address',
#         to_emails='to_email',
#         subject='Your subject or go to SendGrid and create Template',
#         html_content=f'<strong>{text}</strong>')
#     try:
#         sg = SendGridAPIClient(api_key)
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#     except Exception as e:
#         print(e.message)
