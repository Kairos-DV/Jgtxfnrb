import json
import sys
import requests

numbers = []
with open("date.txt", "r") as f:
    for line in f:
        numbers.append(int(line))
print(numbers)
url_beg = "http://numbersapi.com/"
url_end = "/math?json=true"
# url2 = 'http://numbersapi.com/999/math?json=true'
# url3 = 'http://numbersapi.com/43/math?json=true'
for n in numbers:
    res = requests.get(url_beg + str(n) + url_end)
    data = res.json()
    if data['found']:
        print('Interesting')
    else:
        print('Boring')