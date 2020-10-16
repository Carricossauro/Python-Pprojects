from selenium import webdriver
import json

driver = webdriver.Firefox()
driver.get("file:///home/carricossauro/Desktop/Python%20Projects/lcc/cand.html")

dictionary = []
td = 1
while (1):
    pathName = "/html/body/div/table/tbody/tr/td/div[2]/table[4]/tbody/tr[" + str(td) + "]/td[3]"
    pathGrade = "/html/body/div/table/tbody/tr/td/div[2]/table[4]/tbody/tr[" + str(td) + "]/td[4]"
    pathOption = "/html/body/div/table/tbody/tr/td/div[2]/table[4]/tbody/tr[" + str(td) + "]/td[5]"
    try:
        name = driver.find_element_by_xpath(pathName)
        nota = driver.find_element_by_xpath(pathGrade)
        opcao = driver.find_element_by_xpath(pathOption)
    except Exception as error:
        print("No more students. - " + str(error))
        break
    else:
        td+=1
        person = {}
        person['name'] = name.text.encode("utf-8").decode()
        person['grade'] = float(nota.text.replace(',', '.'))
        person['option'] = eval(opcao.text)
        dictionary.append(person)

file = open("candidatos.json", 'w')
json.dump(dictionary, file, ensure_ascii=False, indent=1)
file.close()
driver.close()