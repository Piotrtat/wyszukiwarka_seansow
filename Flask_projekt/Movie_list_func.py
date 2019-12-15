import requests
from bs4 import BeautifulSoup
import re

result = requests.get("https://www.helios.pl/47,Lodz/Repertuar/")
src = result.content
soup = BeautifulSoup(src, 'html.parser')
x = soup.find_all(class_="movie-link")
movies = []
movies2 = []
movies3 = []
movies4 = []

print('*********************************************************************************************')

for link in x:
    t = link.get('href')
    z = t.split('/')
    id = z[6]
    movies2.append(id)
# print(movies2)

for title in movies2:
    l = title.split('?')
    correct_title = l[0]
    if '?' in l:
        continue
    else:
        movies3.append(correct_title)

movies_list = set(movies3)
# print(movies_list)

for title in movies_list:
    with_space = title.replace('-', ' ')
    movies4.append(with_space)
# print(f'Oto lista dostępnych filmów:{movies4}')
# print('*********************************************************************************************\n')

for link in x:
    t = link.get('href')
    z = t.split('/')
    id = z[5:]
    movies.append(id)
# print(movies)

y = soup.find_all(class_="hour-link")
movie_hour = []

for link in y:
    a = link.get('href')
    if a == None:
        continue
    b = a.split('/')
    id_hour = b[-1]
    c = (id_hour, link.text)
    movie_hour.append(list(c))

# print(movie_hour)
new_dict = {}
for movie in movies:
    new_dict[movie[0]] = movie[1]
# print(new_dict)

new_dict2 = {}

for hour in movie_hour:
    if hour[0] in new_dict2:
        new_dict2[hour[0]].append(hour[1])
    else:
        new_dict2[hour[0]] = [hour[1]]
# print(new_dict2)


def final(new_dict, new_dict2):
    print('Oto lista dostępnych seansów w kinie Helios Łodź w dniu dzisiejszym:\n')
    for keys in new_dict.keys():
        j = new_dict.get(keys)
        if '?' in j:
            p = j.replace('?events-filter=only-not-dream', '')
            print(p.replace('-', ' '))
        else:
            print(j.replace('-', ' '))

        godzina = (f'{new_dict2.get(keys, "Brak seansów w dniu dzisiejszym")}\n')
        print(godzina)
    print('*********************************************************************************************')


if __name__ == '__main__':
    final(new_dict, new_dict2)
