import requests

print(requests.__version__)

#r = requests.get("http://www.google.com")
#print(r.status_code)
#print(r.text)

a = requests.get("https://raw.githubusercontent.com/sajjadhaiderrr/CMPUT404-Lab1/master/lab1.py")

print(a.text)
