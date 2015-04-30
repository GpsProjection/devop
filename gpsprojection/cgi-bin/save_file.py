#! C:\Python27\python

import cgi
import pygmaps
import webbrowser
import re
import math
import datetime

def RemoveOutliers(data):
    lowerquartile=percentile(data,0.25)
    upperquartile=percentile(data,0.75)
    interquartile=upperquartile-lowerquartile
    outerfence1=3*interquartile+upperquartile
    outerfence2=lowerquartile-3*interquartile
    for i in data:
        if i<outerfence2 or i>outerfence1:
            data.remove(i)
    return data

def percentile(N, percent, key=lambda x:x):
    N.sort()
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def mean(data):
    return (float(sum(data)/len(data)))

def returnaddress(latitude,longitude):
    import googlemaps
    gmaps = googlemaps.Client(key='AIzaSyBtoNvnBW3rTzn22Dex572VIxcZAoMtaB0')
    reverse_geocode_result = gmaps.reverse_geocode((latitude, longitude))
    return reverse_geocode_result[0]['formatted_address']

def android_test(value):
    flag=0
    lats=[]
    longs=[]
    for each in value:
        if (each!=""):
            each1=each.split()
            if (re.match("[0-9]+",each1[3])):
                lats.append(float(each1[3]))
            if (re.match("[0-9]+",each1[4])):
                longs.append(float(each1[4]))
                
    latitudes=RemoveOutliers(lats)
    longitudes=RemoveOutliers(longs)
    centerlong=mean(longitudes)
    centerlat=mean(latitudes)
    mymap = pygmaps.maps(centerlat,centerlong, 10)
    print "<table border='1'>"
    for each in value:
        if(each != ""):
            print "<html>"
            print "<tr>"
            each1=each.split()
            if(re.match("[0-9]+",each1[3])):
                print "<td>"+each1[3]+"</td>"
                lat=float(each1[3])
                flag=0
            else:
                flag=-1
                print "<th>"+"Latitude&nbsp;&nbsp;"+"</th>"
    					
    					
            if(re.match("[0-9]+",each1[4])):
                print "<td>"+"<br>"+each1[4]+"</td>"
                longitude=float(each1[4])
                flag=0
            else:
                print "<th>"+"Longitude"+"</th>"
                flag=-1

            if flag==-1:
                print "<th>"+"Formatted Address"+"</th>"

            else:
                address=returnaddress(lat,longitude)
                utf_version=address.encode('utf-8')
                print "<td>"+"<br>"+utf_version+"</td>"

    				
            if(re.match("[0-9]+",each1[5])):
                print "<td>"+"<br>"+each1[5]+"</td>"
            else:
                print "<th>"+"Date&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"+"</th>"
                print "<th>"+"Time&nbsp;&nbsp;&nbsp;"+"</th>"
    		
    				
            try:
                print "<td>"+"<br>"+each1[6]+"</td>"
                print "</tr>"
            except:
                print
                
                
            if(flag==0):
                mymap.addradpoint(lat, longitude, 30000, "#FF0000")
                mymap.addpoint(lat, longitude, "#FF0000")
    					
    print "</table>"
    mymap.draw('mymap.draw.html') 
    url = 'mymap.draw.html'
    webbrowser.open_new(url)

def filtering(type,data,value):
    #f=open('cache.cell','r')
    l=value[1:]
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
    android_test(result)
    del result[:] 

def iphone_test(value):
    flag=0
    lats=[]
    longs=[]
    lines=value
    line=lines.split("\n")
    for each in line:
        if (each!=""):
            each1=each.split()
            if (re.match("[0-9]+",each1[5])):
                lats.append(float(each1[5]))
            if (re.match("[0-9]+",each1[6])):
                longs.append(float(each1[6]))
    latitudes=RemoveOutliers(lats)
    longitudes=RemoveOutliers(longs)
    centerlong=mean(longitudes)
    centerlat=mean(latitudes)
    mymap = pygmaps.maps(centerlat,centerlong, 10)
    print "<table border='1'>"
    for each in line:
        if(each != ""):            
            print "<tr>"
            each1=each.split()
            if(re.match("[0-9]+",each1[5])):
                print "<td>"+each1[5]+"</td>"
                lat=float(each1[5])
                flag=0
            else:
                flag=-1
                print "<th>"+"Latitude&nbsp;&nbsp;"+"</th>"                        
                        
            if(re.match("[0-9]+",each1[6])):
                print "<td>"+"<br>"+each1[6]+"</td>"
                longitude=float(each1[6])
                flag=0
            else:
                print "<th>"+"Longitude"+"</th>"
                flag=-1

            if flag==-1:
                print "<th>"+"Formatted Address"+"</th>"

            else:
                address=returnaddress(lat,longitude)
                utf_version=address.encode('utf-8')
                print "<td>"+"<br>"+utf_version+"</td>"
            
            if(flag==0):
                mymap.addradpoint(lat, longitude, 30000, "#FF0000")
                mymap.addpoint(lat, longitude, "#FF0000")

        print "</tr>"

    print "</table>"
    mymap.draw('mymap.draw.html') 
    url = 'mymap.draw.html'
    webbrowser.open_new(url) 
    
def mainplot():
    print "Content-Type: text/html\n\n\n"
    print
    print "<html>"
    print "<h1><font face='Calibri' color='White'><center>GPS DATA PROJECTION</center></font></h1>"
    print "<head>"
    print "<title>Location Extraction</title>"
    print "<style>"
    print "body"
    print "{background-image: url('Forensics_Background.jpg');background-size: 100% 100%;}"
    print "footer"
    print "{width: 100%;bottom: 0;position: fixed;}"
    print "</style>"
    print "</head>"
    print "<body bgcolor= '#FFCC66'>"
    print "<p><b>Filtering Options</b></p>"
    print "<form>"
    print "<p><select>"
    print "<option value='None'>None</option>"
    print "<option value='Time'>Time</option>"
    print "<option value='Date'>Date</option>"
    print "</select>"
    print "<input type='text' name='value_form'></p>"
    print "</form>"
    form_data = cgi.FieldStorage()
    file_data = form_data['myfile'].value
    file_data=file_data.split("\n")
    file_data2=form_data['myfile'].filename
    ext=file_data2.split(".")
    if str(ext[1]) == "cell":
    	android_test(file_data)
        filtering("time","20:03:14",file_data)
    elif str(ext[1]) == "db":
    	iphone_test(file_data)

    print
    print "</body>"
    print "<footer>"
    print "<center><font color='white'>&copyProject conceptualised and developed by Sanjana Ramprasad, Sharath Sreenivasan and Shrikanth Kainthaje. Copyright protected.</font></center>"
    print "<br>"
    print "</footer>"
    print "</html>"

if __name__ == '__main__':
    mainplot() 