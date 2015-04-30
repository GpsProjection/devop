import datetime,re


def some_function(type,data):
	f=open('cache.cell','r')
	l=f.readlines()[1:]
	result=[]
	for line in l:
		lines=re.split("\s+",line)

		if type=='time':
			comparator=datetime.datetime.strptime(data, "%H:%M:%S")
			#print comparator
			for value in lines:
				if re.findall('[0-9]+:[0-9]+:[0-9][0-9]$',value):
					c=datetime.datetime.strptime(value, "%H:%M:%S")
					if c == comparator:
						#print "here"
						result.append(line)

		elif type=='date':
			comparator=datetime.datetime.strptime(data, "%m/%d/%y").date()
			for value in lines:
				if re.match('[0-9]+/[0-9]+/[0-9]+$',value):
					#print value
					date=datetime.datetime.strptime(value, "%m/%d/%y").date()
					if comparator == date:
						result.append(line)
	return result
	del result[:]
						

	
if __name__=='__main__':
	#specify type of filtering and comparator
	result=some_function("time","20:03:14")
	result2=some_function("date","04/11/11")
	print result
	print result2