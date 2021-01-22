# Platform
from sys import platform
import os

def chrome_version():
    
	if platform == 'darwin':
		installpath = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
	elif platform == 'win32':
		installpath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
	elif platform == 'linux':
		installpath = "/usr/bin/google-chrome"
	else:
		raise NotImplemented(f"Unknown OS '{osname}'")
				
	verstr = os.popen(f"{installpath} --version").read().strip('Google Chrome ').strip()
	
	return verstr