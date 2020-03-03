import json
from urllib.request import urlopen
from urllib.parse import quote


def getInfo(movie):
    url = 'http://www.omdbapi.com/?apikey=62465380&t=' + quote(movie)
    jsonurl = urlopen(url)
    info = json.load(jsonurl)
    if info['Response'] == 'True':
        title = info['Title']
        date = getReleaseDate(info['Released'])
        runtime = int(info['Runtime'].split(' ')[0])
        return convertToString((title, runtime, date))
    else:
        return None


def getReleaseDate(text):
    words = text.split(' ')
    ret = words[2] + '-' + month(words[1]) + '-' + words[0]
    return ret


def convertToString(tuple):
    string = "('" + tuple[0] + "', " + str(tuple[1]) + ", '" + tuple[2] + "')"
    print(string)
    return string


def month(m):
    month = 0
    if m == 'Jan':
        month = 1
    elif m == 'Feb':
        month = 2
    elif m == 'Mar':
        month = 3
    elif m == 'Apr':
        month = 4
    elif m == 'May':
        month = 5
    elif m == 'Jun':
        month = 6
    elif m == 'Jul':
        month = 7
    elif m == 'Aug':
        month = 8
    elif m == 'Sep':
        month = 9
    elif m == 'Oct':
        month = 10
    elif m == 'Nov':
        month = 11
    elif m == 'Dec':
        month = 12
    return str(month)


if __name__ == '__main__':
    movie = input("Name: ")
    a = getInfo(movie)
    print(a)