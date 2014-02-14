import requests
import re
import json
from bs4 import BeautifulSoup


postalCodes = {}
states = {}

states = json.loads(open("state-flags.json").read())

soup = BeautifulSoup(requests.get("http://www.sochi2014.com/en/medal-standings").text)

rows = soup.find("div",class_="standings").find("table").find_all("tr")

countries = []

for row in rows[1:]:

	cells = row.find_all("td")[1:]

	country = {
		"flagClass": cells[0]["class"][-1],
		"name": cells[0].find("a").text.strip(),
		"gold": int(cells[1].text),
		"silver": int(cells[2].text),
		"bronze": int(cells[3].text),
		"total": int(cells[4].text),
		"country": 1
	}

	if country["name"] != "United States":
		countries.append(country)

print countries

# scrape this page: http://www.teamusa.org/2014teamusa