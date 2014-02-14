import requests
from bs4 import BeautifulSoup
import re
import json

postalCodes = {}
states = {}

soup = BeautifulSoup(open("flagtable.html").read())

abbreviations = json.loads(open("abbreviations.json").read())

for a in abbreviations:
	postalCodes[a["State"]] = a["Abbreviation"]

innerTables = soup.find_all("table")

i = 0

for table in innerTables:
#	print table
	if table.find_all("table"):
		continue

	img = table.find("img")["src"]

	if not re.match("http",img):
		img = "http:"+img

	lastCell = table.find_all("td")[-1]
	
	if re.search("reverse",lastCell.text):
		continue

	for link in lastCell.find_all("a"):
		if link.text == "Flag":
			continue
		if re.search(".?cite",link["href"]):
			continue

		print link.text.strip()

		states[link.text.strip()] = {
			"abbreviation": postalCodes[link.text.strip()],
			"img": img,
			"medals": {
				"total": 0,
				"gold": 0,
				"silver": 0,
				"bronze": 0
			}
		}

print json.dumps(states)