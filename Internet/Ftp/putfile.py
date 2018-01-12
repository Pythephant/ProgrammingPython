from ftplib import FTP

def putfile(fileName, site, remoteDir, user=(), *,verbose=True):
	if verbose:
		print('Uploading',fileName)
	local = open(fileName, 'rb')
	remote = FTP(site)
	remote.login(*user)
	remote.cwd(remoteDir)
	remote.storbinary('STOR '+fileName,local,1024)
	remote.quit()
	local.close()
	if verbose:
		print('Uploading done')

if __name__ == '__main__':
	import sys , getpass
	site = input('remote site:')
	fileName = input('File to Upload:')
	user = (input('User:'), getpass.getpass())
	if not user[1]:
		user = ()
	putfile(fileName, site, '.', user)
