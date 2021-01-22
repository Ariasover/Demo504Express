# Platform
from sys import platform
import os

def get_platform_architecture():
    if sys.platform.startswith('linux') and sys.maxsize > 2 ** 32:
        platform = 'linux'
        architecture = '64'
    elif sys.platform == 'darwin':
        platform = 'mac'
        architecture = '64'
    elif sys.platform.startswith('win'):
        platform = 'win'
        architecture = '32'
    else:
        raise RuntimeError('Could not determine chromedriver download URL for this platform.')
    return platform, architecture

def get_chrome_version():
    """
    :return: the version of chrome installed on client
    """
    platform, _ = get_platform_architecture()
    if platform == 'linux':
        executable_name = 'google-chrome'
        if os.path.isfile('/usr/bin/chromium-browser'):
            executable_name = 'chromium-browser'
        if os.path.isfile('/usr/bin/chromium'):
            executable_name = 'chromium'
        with subprocess.Popen([executable_name, '--version'], stdout=subprocess.PIPE) as proc:
            version = proc.stdout.read().decode('utf-8').replace('Chromium', '').replace('Google Chrome', '').strip()
    elif platform == 'mac':
        process = subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version'], stdout=subprocess.PIPE)
        version = process.communicate()[0].decode('UTF-8').replace('Google Chrome', '').strip()
    elif platform == 'win':
        process = subprocess.Popen(
            ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL
        )
        version = process.communicate()[0].decode('UTF-8').strip().split()[-1]
    else:
        return
    return version
# def chrome_version():
    
# 	if platform == 'darwin':
# 		installpath = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"
# 	elif platform == 'win32':
# 		installpath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# 	elif platform == 'linux':
# 		installpath = "/usr/bin/google-chrome"
# 	else:
# 		raise NotImplemented(f"Unknown OS '{osname}'")
				
# 	verstr = os.popen(f"{installpath} --version").read().strip('Google Chrome ').strip()
	
# 	return verst

