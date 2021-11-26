import requests
from bs4 import BeautifulSoup

country = "Turkey"
country = country.lower()

headers = {'User-Agent': 'Mozilla/5.0'}
url = f"https://www.worldometers.info/world-population/{country}-population/"
content = requests.get(url, headers=headers).content
soup = BeautifulSoup(content, "html.parser")

result = soup.find_all("strong")

population = int(result[1].text.replace(",", ""))

print(population)
