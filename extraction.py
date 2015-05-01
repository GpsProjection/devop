import ftplib,cgi
def ftpConnect(username,password,ip,port):
	ftp = ftplib.FTP()
	ftp.connect(str(ip),int(port))
	ftp.login(str(username),str(password))
	#c=ftp.dir()
	#print ftp.retrlines('LIST')
	ftp.retrbinary('RETR cache.cell', open('cache.cell', 'wb').write)

if __name__=='__main__':
	form = cgi.FieldStorage() 
	username = form.getvalue('username')
	password = form.getvalue('password')
	ip = form.getvalue('ip')
	port = form.getvalue('port')
	ftpConnect(username,password,ip,port)

