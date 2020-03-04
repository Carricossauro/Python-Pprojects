import requests
from lxml import html

site = "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"
page = requests.get(site)
tree = html.fromstring(page.content)
name = tree.xpath("/html/body/div[1]/main/div/div/div[4]/div/table[2]/tbody/tr[2]/td[2]/a/text()")
print(name)
