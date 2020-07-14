import requests
from bs4 import BeautifulSoup
r = requests.get("https://test.com")# make sure you have either https or http
c = r.content
soup = BeautifulSoup(c,'html.parser')
