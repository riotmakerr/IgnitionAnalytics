import os
dir = 'C:\\Ignition\\Hand History\\14074647';

# stat_type can be STT or MTT
def getStats(stattype):
	sttplayed = 0
	totalcash = 0
	totalbuyin = 0

	# $0-10, $11-99, $100+
	buyins = [0, 0, 0]
	cashes = [0, 0, 0]

	for file in os.listdir(dir):
	    if file.endswith(".txt"):
	    	if ('- ' + stattype + ' -' in file):
	    		sttplayed = sttplayed + 1
	    		buyin = file.split(' - ')[4]
	    		if(buyin[1] != '0'): # exclude freeroll case for rake
	    			r = buyin.split('-')[1]
	    			buyin = buyin.split('-')[0]
	    			if(buyin.find('TT') >= 0): # Tournament Ticket (might track later)
	    				buyin = buyin[2:]
	    			buyin = float(buyin[1:len(buyin)]) + float(r[1:len(r)])
	    			if(buyin < 10):
	    				buyins[0] = buyins[0] + buyin
	    			elif(buyin > 10 and buyin < 100):
	    				buyins[1] = buyins[1] + buyin
	    			elif(buyin > 100):
	    				buyins[2] = buyins[2] + buyin
	    			totalbuyin = totalbuyin + buyin
	    		for line in open(dir + '//' + file):
	    			if '[ME] : Prize Cash' in line:
	    				i = line.find('$')+1
	    				cash = float(line[i:i+line[i:len(line)].find(']')])
	    				totalcash = totalcash + cash
	    				if(buyin < 10):
	    					cashes[0] = cashes[0] + cash
	    				elif(buyin > 10 and buyin < 100):
	    					cashes[1] = cashes[1] + cash
	    				elif(buyin > 100):
	    					cashes[2] = cashes[2] + cash

	print ' '  					
	print stattype, 'played:', sttplayed
	print ' Total Profit: $' , (totalcash - totalbuyin)
	print ' Combined ROI =' , round(((totalcash - totalbuyin) / totalbuyin) * 100, 2), '%'
	print ' '

	if(buyins[0] != 0):
		print ' $1-$10 Profit: $' , (cashes[0] - buyins[0])
		print ' $1-$10 ROI =' , round(((cashes[0] - buyins[0]) / buyins[0]) * 100, 2), '%'
		print ' '
	if(buyins[1] != 0):
		print ' $10-$100 Profit: $' , (cashes[1] - buyins[1])
		print ' $10-$100 ROI =' , round(((cashes[1] - buyins[1]) / buyins[1]) * 100, 2), '%'
		print ' '
	if(buyins[2] != 0):
		print ' $100+ Profit: $' , (cashes[2] - buyins[2])
		print ' $100+ ROI =' , round(((cashes[2] - buyins[2]) / buyins[2]) * 100, 2), '%'
		print ' '



getStats('MTT')
getStats('STT')


