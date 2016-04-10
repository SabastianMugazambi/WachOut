import csv

def crimeString (X, Y):
	info = ""
	newX = int(round((X - 40.4)/.001))
	newY = int(round((Y + 74.3)/.002))
	#print newX, newY


	with open('AllCrimes.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					allCrimes = row[newY]
					break
				else: 
					a = a + 1

	with open('Assault.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					assault = row[newY]
					break
				else: 
					a = a + 1

	with open('Burglary.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					burglary = row[newY]
					break
				else: 
					a = a + 1

	with open('Grand_Larceny.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					larceny = row[newY]
					break
				else: 
					a = a + 1

	with open('GTA.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					gta = row[newY]
					break
				else: 
					a = a + 1

	with open('Rape.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					rape = row[newY]
					break
				else: 
					a = a + 1

	with open('Robbery.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					robbery = row[newY]
					break
				else: 
					a = a + 1

	with open('Murder.csv', 'rb') as csvfile:
		crimes = csv.reader(csvfile, delimiter = ',', quotechar = '|')
		a = 1
		for row in crimes:
			if a == 1:
				#print row[newY]
				a = a + 1
			else:
				if float(row[0][1:-1]) == X:
					#print row[0]
					murder = row[newY]
					break
				else: 
					a = a + 1


	info = '''
	In the last five years, there have been:
	%s felonies
	%s assaults
	%s burglaries
	%s instances of grand larceny
	%s instances of grand theft auto
	%s murders
	%s instances of rape
	%s robberies
	''' %(allCrimes, assault, burglary, larceny, gta, murder, rape, robbery)

	return info


print crimeString(40.61, -73.924)