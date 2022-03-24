import requests
import string
import random

####### create cities
cities = []

r = requests.get('https://api.hh.ru/areas')
pk = 0
for j in r.json()[0]['areas']:
    for i in j['areas']:
        cities.append({"model": "netrikatest.city",
                       "fields": {
                           "cityname": i['name']
                       }})
with open('netrikatest/fixtures/addcities.json', 'w') as cityfile:
    cityfile.write(str(cities).replace('\'', '\"'))
citylen = len(cities)
# create people

peoples = []

names = ["Ivan", "Petr", "Vasilii", "Alexey", "Fedor", "Maksim", "Irina", "Anastasia", "Elena", "Darya", "Demyan",
         "Roman", "Kirill", "Ekaterina", "Sofia", "Gleb", "Marfa"]
surnames = ["Cher", "Kipelov", "Petrov", "Ivanov"]
for i in range(10000):
    firstletter = random.choice(string.ascii_uppercase)
    letters = string.ascii_lowercase
    newsurname = firstletter
    for j in range(i % 7):
        newsurname += random.choice(letters)
    surnames.append(newsurname)

for i in range(50000):
    cityid = random.randint(1, citylen)
    fullname = (random.choice(names) + " " + random.choice(surnames))
    peoples.append({"model": "netrikatest.people", "fields":{"fio": fullname, "city": cityid}})
with open('netrikatest/fixtures/addpeople.json', 'w') as peoplefile:
    peoplefile.write(str(peoples).replace('\'', '\"'))


