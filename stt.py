import os
dir = 'C:\\Ignition\\Hand History\\14074647';

def getStats(stattype):
	sttplayed = 0
	totalcash = 0
	totalbuyin = 0
	for file in os.listdir(dir):
	    if file.endswith(".txt"):
	    	if ('- ' + stattype + ' -' in file):
	    		sttplayed = sttplayed + 1
	    		buyin = file.split(' - ')[4]
	    		if(buyin[1] != '0'): # exclude freeroll case for rake
	    			b = buyin.split('-')[0]
	    			r = buyin.split('-')[1]
	    			if(b.find('TT') >= 0): # Tournament Ticket (might track later)
	    				b = b[2:]
	    			totalbuyin = totalbuyin + float(b[1:len(b)]) + float(r[1:len(r)])
	    		for line in open(dir + '//' + file):
	    			if '[ME] : Prize Cash' in line:
	    				i = line.find('$')+1
	    				totalcash = totalcash + float(line[i:i+line[i:len(line)].find(']')])
	print stattype, 'played:', sttplayed
	print 'profit: $' , (totalcash - totalbuyin)
	print 'ROI =' , ((totalcash - totalbuyin) / totalbuyin) * 100, '%'
	print ' '



getStats('MTT')
getStats('STT')


