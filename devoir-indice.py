# ©2018 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

import csv, os, glob

nb = input("On travaille sur des segments de combien de mots?")
nb = int(nb)

fichiers = glob.iglob("liste-mots/token2/*.csv")
fichOUTPUT = "devoir-indice-a-{}.csv".format(str(nb))
thesaurus1 = []
thesaurus2 = []

f1 = open("thesaurus_1.csv")
t1 = csv.reader(f1)
next(t1)
for m1 in t1:
	thesaurus1.append(m1)

f2 = open("thesaurus_2.csv")
t2 = csv.reader(f2)
next(t2)
for m2 in t2:
	thesaurus2.append(m2)

for fichier in fichiers:
	indice_total = 0
	print(fichier)
	f3 = open(fichier)
	mots = csv.reader(f3)
	tousmots = []
	tousmotsNB = []
	for mot in mots:
		tousmots.append(mot[0])
	# print(tousmots)
	for x in range(0,len(tousmots),nb):
		tousmotsNB.append(tousmots[x:x+nb])
	# print(tousmotsNB)
	for groupedeNB in tousmotsNB:
		# print("On examine {}".format(groupedeNB))
		indice = 0
		for culture1 in thesaurus1:
			if culture1[0] in groupedeNB:
				# print("On a trouvé le mot {} dans {}".format(culture1[0],fichier))
				indice += int(culture1[4])
				# ok = input("On continue?")
				# print("L'indice local est à {}".format(str(indice)))
				c2 = 0
				# print("On cherche dans le thesaurus2")
				for culture2 in thesaurus2:
					if culture2[0] in groupedeNB:
						# print("   On trouve le mot {}".format(culture2[0]))
						c2 += 1
						indice += int(culture2[4])
						# print("   L'indice local est à {}".format(str(indice)))
						# print(culture2[0],groupedeNB,indice_total,indice,c2)
						# ok = input("On continue?")
					# else:
					# 	print("   On trouve aucun mot")
				if c2 == 0:
					# print("   Aucun mot du thesaurus2 dans ce groupe de {}".format(nb))
					indice = 0
					# ok = input("On continue?")
				else:
					indice_total += indice
					# print("   L'indice total passe à {}".format(indice_total))
					# ok = input("On continue?")
	# print(len(tousmots),indice,round(indice/len(tousmots)*100,2))
	fichdecompose = fichier.split("-")
	date = fichdecompose[3][:8]
	lindice = [date[:4],date[4:6],date[6:8],len(tousmots),indice_total,round(indice_total/len(tousmots)*100,2)]
	print(lindice)
	# henri = open(fichOUTPUT, "a")
	# bourassa = csv.writer(henri)
	# bourassa.writerow(lindice)