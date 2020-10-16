from selenium import webdriver
import json


driver = webdriver.Firefox()
driver.get("file:///home/carricossauro/Desktop/Python%20Projects/lcc/cols.html")

dictionary = []
td = 1
while (1):
    path = "/html/body/div/table/tbody/tr/td/div[2]/table[3]/tbody/tr[" + str(td) + "]/td[2]"
    try:
        name = driver.find_element_by_xpath(path)
    except Exception as error:
        print("No more students. - " + str(error))
        break
    else:
        td+=1
        person = name.text.encode("utf-8").decode()
        dictionary.append(person)

file = open("colocados.json", 'w')
json.dump(dictionary, file, ensure_ascii=False, indent=1)
file.close()

driver.close()