import requests
from bs4 import BeautifulSoup
import re

def current_movie_list():
    result = requests.get("https://www.helios.pl/47,Lodz/Repertuar/")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    x = soup.find_all(class_="movie-link")
    movies = []
    movies2 = []
    movies3 = []
    movies4 = []

    global new_dict, new_dict2
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
    return movies4

def final(dict1, dict2):
    lista = []
    print('Oto lista dostępnych seansów w kinie Helios Łodź w dniu dzisiejszym:\n')
    for keys in dict1.keys():
        j = dict1.get(keys)
        if '?' in j:
            p = j.replace('?events-filter=only-not-dream', '')
            i = p.replace('-', ' ')
            lista.append(i)
        else:
            o = j.replace('-', ' ')
            lista.append(o)
        godzina = (f'{dict2.get(keys, "Brak seansów w dniu dzisiejszym")}')
        lista.append(godzina)
    #     print(godzina)
    # print('*********************************************************************************************')
    # print(lista)
    return lista


def run_search():
    result = requests.get("https://www.helios.pl/47,Lodz/Repertuar/")
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    x = soup.find_all(class_="movie-link")
    movies = []
    movies2 = []
    movies3 = []
    movies4 = []

    global new_dict, new_dict2
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
    print(f'Oto lista dostępnych filmów:{movies4}')
    print('*********************************************************************************************\n')

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
    print(new_dict)

    new_dict2 = {}
    for hour in movie_hour:
        if hour[0] in new_dict2:
            new_dict2[hour[0]].append(hour[1])
        else:
            new_dict2[hour[0]] = [hour[1]]

    godziny = final(new_dict, new_dict2)
    return godziny


if __name__ == '__main__':
    run_search()
    # final(new_dict, new_dict2)
    current_movie_list()