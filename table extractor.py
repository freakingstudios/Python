import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/tags/tag_table.asp"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

tables = soup.find_all("table")
for table in tables:
    print(table)
