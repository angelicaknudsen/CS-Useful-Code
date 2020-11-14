#Code for Moon Base L4 C4 "Unlocking the Message"

#I'm just saving this one since it was really tough for me
#This probably isn't allowed, but whatevs


# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout if this occurs try narrowing
# down your search
#

import urllib.request

url = "http://127.0.0.1:8082"

for x in range(5500, 5601):
  key = str(x)
  hdr = {"x-api-key" : key}
  req = urllib.request.Request(url, headers=hdr)
  response = urllib.request.urlopen(req)
  print(response.read())