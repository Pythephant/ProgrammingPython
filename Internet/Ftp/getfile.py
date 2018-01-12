from ftplib import FTP
import os

def getfile(fileName, site, remoteDir, user=(), *, verbose=False, refetch=False):
	if os.path.exists(fileName) and not refetch:
		print('%s has already exists!'%fileName)
	else:
		if verbose:
			print('Downloading file', fileName)
		try:
			local = open(fileName, 'wb')
			remote = FTP(site)
			remote.login(*user)
			remote.cwd(remoteDir)
			remote.retrbinary('RETR '+fileName, local.write, 1024)
		finally:
			remote.quit()
			local.close()

		if verbose:
			print('Download done.')

if __name__ == '__main__':
	from getpass import getpass
	site = input('remote ftp site:')
	user = ()
	fileName = 'pics'
	getfile(fileName, site, '.',user, verbose=True)
