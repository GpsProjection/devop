import ftplib
ftp = ftplib.FTP()
ftp.connect('192.168.1.4', 2221)
ftp.login('francis','francis')
#c=ftp.dir()
#print ftp.retrlines('LIST')
ftp.retrbinary('RETR cache.cell', open('cache.cell', 'wb').write)