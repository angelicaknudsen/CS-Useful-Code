import urllib2

link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!

password = urllib2.urlopen(link)
pswd = password.read()
revString = ''.join(reversed(pswd))


answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib2.urlopen(answer)
response = response.read()
print(response)
