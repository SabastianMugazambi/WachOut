from flask import Flask
app = Flask(__name__)
import csv

@app.route("/")
def homepage():
    return crimeString(40.776641,-73.952147)
    #return "Daniel is a badass"

# @app.route("/introuble/<position>")
# def getHelp(position):


@app.route('/<position1>/<position2>')
#def crimeDataRetrieval():
def splitPosition(position1,position2):
	#newPositions = position.split('?')
	X = float (position1)
	Y = float (position2)
	return crimeString(X,Y)

def crimeString (X, Y):

	if X<40.49 or X >40.92 or Y > -73.7 or Y < -74.3 :
		return "Coming to this location soon"

	info = ""
	newX = int(round((X - 40.4)/.001))
	newY = int(round((Y + 74.3)/.002))
	#print newX, newY
	X = round(X, 3)

	allCrimes = "You are currently not in NYC"
	assault = allCrimes
	burglary = allCrimes
	larceny = allCrimes
	gta = allCrimes
	rape = allCrimes
	robbery = allCrimes
	murder = allCrimes


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
	theList = []
	theList.append('Felonies:'+ allCrimes)
	if int(burglary) >= 3:
		theList.append('Burglaries:'+ burglary)
	if int(assault) >= 3.5:
		theList.append('Assaults:'+ assault)
	if int(larceny) >= 14:
		theList.append('GrandLarceny:' + larceny)
	if int(gta) >= 1.1:
		theList.append('Gta:' + gta)
	if int(rape) >= 3.5:
		theList.append('Rape' + rape)
	if int(robbery) >= 3.3:
		theList.append('Roberies' + robbery)
	if int(murder) >= 1:
		theList.append('Murder' +murder)

	info = ", ".join(theList[:3])
	# info = '''
	# Felonies: %s, Burglaries: %s , Assaults: %s , GrandLarceny: %s , Gta: %s , Murder: %s , Rape: %s , Robberies: %s
	# ''' %(allCrimes, burglary, assault, larceny, gta, murder, rape, robbery)

	return info





if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
