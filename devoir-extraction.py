# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob, requests, textract
from stopwords import stop
import nltk
from nltk.tokenize import word_tokenize

source = "devoir-source-des-pdf.csv"

entetes = {
	"User-Agent":"Jean-Hugues Roy - requête transmise pour un projet de recherche avec les Cahiers du journalisme",
	"From":"roy.jean-hugues@uqam.ca"
}

fr = 0
nonFr = 0
nb = 0

f1 = open(source)
dates = csv.reader(f1)
next(dates)

for date in dates:
	m = 0
	print("&"*66)
	urlFichier = "http://collections.banq.qc.ca/{}".format(date[8])
	# print(urlFichier)

	nomFichier = os.path.basename(urlFichier)
	# print(nomFichier)

	print("On va chercher le fichier {}\nà l'URL {}".format(nomFichier,urlFichier))

	pdf = requests.get(urlFichier, stream=True, headers=entetes)

	with open("pdfs/{}".format(nomFichier), 'wb') as fuddle:
		for chunk in pdf.iter_content(100):
			fuddle.write(chunk)

	nom = nomFichier.split("_")

	if len(nom) > 2:
		code = nom[2].strip(".pdf")
		outputCSV = "liste-mots/ledevoir-token2-{}{}{}_{}.csv".format(date[1][:4],date[1][5:7],date[1][8:10],code)
		outputTXT = "liste-mots/ledevoir-brut-{}{}{}_{}.txt".format(date[1][:4],date[1][5:7],date[1][8:10],code)
	else:
		outputCSV = "liste-mots/ledevoir-token2-{}{}{}.csv".format(date[1][:4],date[1][5:7],date[1][8:10])
		outputTXT = "liste-mots/ledevoir-brut-{}{}{}.txt".format(date[1][:4],date[1][5:7],date[1][8:10])

	print("On commence à créer les fichiers {} et {}".format(outputCSV,outputTXT))

	texte = textract.process("pdfs/{}".format(nomFichier))

	mots = word_tokenize(texte.decode('utf-8'))
	print(mots)
	print(len(mots))

	with open(outputTXT, "w") as duddle:
		duddle.write(str(mots))
	
	debut = ""
	x = 0
	for mot in mots:
		mot = debut + mot
		if "\xad" in mot:
			debut = mot.replace("\xad","")
			x = 1
			nb += 1
		else:
			debut = ""
			x = 0
		mot = mot.lower()
		
		if mot not in stop:
			if mot.isalpha():
				if len(mot) > 1:
					m += 1
					phrase = [mot]
					print("   >>> Mot «{}» imprimé le {}".format(mot,date[2]))

					ying = open(outputCSV, "a")
					yang = csv.writer(ying)
					yang.writerow(phrase)

	print("Il y avait {} mots dans le fichier {}".format(str(m),nomFichier))
	
	os.remove("pdfs/{}".format(nomFichier))
