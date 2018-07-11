# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, requests, json

fich = "devoir-api-2.csv"

n=0
for x in range(2806457,2930478):
	n += 1
	print(x,n)

	entetes = {
		"User-Agent":"Jean-Hugues Roy - requête transmise pour un projet de recherche avec les Cahiers du journalisme",
		"From":"roy.jean-hugues@uqam.ca"
	}
	url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/{}".format(x)
	req = requests.get(url,headers=entetes)
	print(req.status_code)

	if req.status_code == 200:
		info = req.json()
		if info["titre"] == "Le devoir, 1910- (Montréal)":
			edition = []
			edition.append(url)
			edition.append(info["annee"])
			edition.append(info["mois"])
			edition.append(info["jour"])
			edition.append(info["bitstreams"]["liste"][0]["url"])
			edition.append(info["bitstreams"]["liste"][0]["fichier"])
			edition.append(info["bitstreams"]["liste"][0]["size"])

			print(edition)
			ying = open(fich, "a")
			yang = csv.writer(ying)
			yang.writerow(edition)