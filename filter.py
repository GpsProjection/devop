import re
from geopy.geocoders import Nominatim
import datetime
def filtering(type,data,value):
    l=value[1:]
    result=[]
    for line in l:
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
            comparator=datetime.datetime.strptime(data, "%m/%d/%y").date()
            if re.match('[0-9]+/[0-9]+/[0-9]+$',date_file):
                #print value
                date=datetime.datetime.strptime(date_file, "%m/%d/%y").date()
                if comparator == date:
                    result.append(line)

        elif type=='location':
            geolocator = Nominatim()
            location = geolocator.geocode("175 5th Avenue NYC")
            try:
                comparator=data.lower()
                geolocator = Nominatim()
                location = geolocator.geocode(comparator)
                latitude=location.latitude
                longitude=location.longitude
                print latitude,longitude
                if latitude==latitude_file and longitude==longitude_file:
                    print "ayyy"
                    result.append(line)
            except:
                print "lakd"
            for value in lines:
                if comparator==value:
                    result.append(line)

    return result




    #android_test(result)
    del result[:] 
