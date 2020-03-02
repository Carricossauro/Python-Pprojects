from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def main():
    movie = input("Movies: ")
    ab = scrape(movie)


def scrape(movie):
    time = None
    driver = webdriver.Firefox()
    driver.get("https://www.imdb.com")

    print("Getting movie information...")
    search(driver, movie)

    getDate = driver.find_element_by_css_selector('div.txt-block:nth-child(6)').text
    date = getReleaseDate(getDate)

    print("Movie release date retrieved - " + date)

    try:
        getTime = driver.find_element_by_css_selector('div.txt-block:nth-child(23) > time:nth-child(2)').text
        time = getRunTime(getTime)
    except NoSuchElementException as error:
        print(str(error) + "Trying: div.txt-block:nth-child(22) > time:nth-child(2)")
        try:
            getTime = driver.find_element_by_css_selector('div.txt-block:nth-child(22) > time:nth-child(2)').text
            time = getRunTime(getTime)
        except NoSuchElementException as error:
            print(str(error) + "Trying: div.txt-block:nth-child(21) > time:nth-child(2)")
            try:
                getTime = driver.find_element_by_css_selector('div.txt-block:nth-child(21) > time:nth-child(2)').text
                time = getRunTime(getTime)
            except NoSuchElementException as error:
                print("Failed in getting runtime: " + str(error))
            else:
                print("Movie runtime retrieved - " + time)    
        else:
            print("Movie runtime retrieved - " + time)
    else:
        print("Movie runtime retrieved - " + time)

    driver.close()
    return convertToString((movie, time, date))


def getRunTime(time):
    words = time.split(' ')
    return words[0]


def search(driver, movie):
        search = driver.find_element_by_xpath('//*[@id="suggestion-search"]')
        search.send_keys(movie)
        searchButton = driver.find_element_by_xpath('//*[@id="suggestion-search-button"]')
        searchButton.click()
        movieURL = driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]/a')
        movieURL.click()


def getReleaseDate(text):
    words = text.split(' ')
    ret = words[4] + '-' + month(words[3]) + '-' + words[2]
    return ret


def month(m):
    month = 0
    if m == 'January':
        month = 1
    elif m == 'February':
        month = 2
    elif m == 'March':
        month = 3
    elif m == 'April':
        month = 4
    elif m == 'May':
        month = 5
    elif m == 'June':
        month = 6
    elif m == 'July':
        month = 7
    elif m == 'August':
        month = 8
    elif m == 'September':
        month = 9
    elif m == 'October':
        month = 10
    elif m == 'November':
        month = 11
    elif m == 'December':
        month = 12
    return str(month)


def convertToString(tuple):
    string = "('" + tuple[0] + "', " + tuple[1] + ", '" + tuple[2] + "')"
    print(string)
    return string


if __name__ == '__main__':
    main()
