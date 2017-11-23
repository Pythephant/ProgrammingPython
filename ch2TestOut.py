'''
this is a test script to check the os.getcwd()
when the sorce code(A) is invoke by another script(B)
the os.getcwd() in the A is return the current path of the B
'''
from System.testIn import printPath
import os

if __name__ == '__main__':
	print(os.getcwd())
	printPath()
