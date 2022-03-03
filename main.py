import requests


URL = 'https://www.lego.com/en-sg/themes/marvel'
# Task5.1
url = 'http://www.wikipedia.org'
r = requests.get(url)
print(r.text)
print("**********")

# Task 5.2
print("Status.code.")
print("\t*", r.status_code)
if r.status_code == 200:
    print("OK!")
else:
    print("Error")

# Task 5.3 & 5.4
h = requests.head(url)
print("***********")
print("Header.")
for x in h.headers:
    print("\t", x, ":", h.headers[x])
print("******")
headers = {
    'User-Agent': 'Mobile'
}

url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)




