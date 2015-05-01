import re
import geocoder
import datetime
#filea=open('cache.cell','r')
#lister=filea.readlines()
#print lister

def filtering(type,data,value):
    l=value[1:]
    result=[]
    count=0
    count1=0
    for line in l:
        count1=count1+1
        lines=re.split("\s+",line)
        print lines
        latitude_file=lines[3]
        longitude_file=lines[4]
        time_file=lines[6]
        date_file=lines[5]
        print latitude_file,longitude_file,time_file,date_file
        
        if type=='time':
            comparator=datetime.datetime.strptime(data, "%H:%M:%S")
            if re.findall('[0-9]+:[0-9]+:[0-9][0-9]$',time_file):
                c=datetime.datetime.strptime(time_file, "%H:%M:%S")
                print "C",c,comparator
                if c == comparator:
                    #print "here"
                    result.append(line)

        elif type=='date':
            comparator=datetime.datetime.strptime(data, "%d-%m-%Y").strftime("%m/%d/%y")
            comparing=datetime.datetime.strptime(comparator, "%m/%d/%y").date()
            if re.match('[0-9]+/[0-9]+/[0-9]+$',date_file):
                date=datetime.datetime.strptime(date_file, "%m/%d/%y").date()
                if comparing == date:
                    result.append(line)

        
        
        elif type=='location':
                location_file = geocoder.google([latitude_file,longitude_file], method='reverse')
                print location_file
                comparator=data.lower()
                if re.findall(comparator,str(location_file).lower()):
                    count=count+1
                    result.append(line)

    print "Count",count,count1
    return result




    #android_test(result) 
#result=filtering('location','BASAVANAGUDI',lister)
#print "RESULT",result
