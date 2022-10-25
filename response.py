import requests
import json
from bs4 import BeautifulSoup


def get_html_string(obj, mn=None, week=None):
    params = dict(obj=obj, mn=mn, week=week)
    response = requests.get('https://lk.ks.psuti.ru/', params=params)
    return response.text


soup = BeautifulSoup(get_html_string(<object>), features="html.parser")


def get_days_of_week(soup):

    days = soup.find_all(
        'td', {'colspan': '7', 'height': '20', 'bgcolor': 'C0D8E3'})
    result = {}
    for day in days:
        day_of_week = day.find('td', {'bgcolor': '3481A6'}).find('h3').text
        result[day_of_week] = {}
    return result.keys()


def get_json(soup):
    rows = soup.find_all('tr', {'align': 'center'})
    i = 0
    data = [[]]
    for row in rows[1:]:
        columns = row.find_all('td', {'bgcolor': ['ffffff', 'ffffbb']})
        if columns[0].text == '№ пары':
            i += 1
            data.append([])
        else:
            maps_list = list(map(lambda x: x.text, columns))
            temp = ''
            if columns[3].find('a', {'class': 't_zm'}):
                pass
            else:
                for j, item in enumerate(columns[3].contents):
                    if j % 2 != 0:
                        item = '\n'
                    temp += item
                maps_list[3] = temp
            data[i].append(maps_list)

    keys = ['number', 'time', 'method', 'name', 'issue', 'resource', 'task']
    week_days = get_days_of_week(soup)
    result = {}
    for day, item in zip(week_days, data):
        result[day] = {}
        for m, query in enumerate(item):
            result[day][m] = dict(zip(keys, query))
    return result


with open("result.json", 'w+') as file:
    dump = get_json(soup)
    json.dump(dump, file, indent=4, ensure_ascii=False)