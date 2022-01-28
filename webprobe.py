from sys import argv
import threading
import requests
import argparser

# To suppress SSL warnings.
from requests.packages import urllib3
urllib3.disable_warnings()

no_threads = 5
arguments = ["--thread", "-t", "-o", "--output"]
"""
# Usage:
# python3 webprobe.py <SampleFile> 
# python3 webprobe.py --thread <NoOfThreads> <SampleFile>
"""
parser=argparse.ArgumentParser(description='WebProber V1.0')
parser.add_argument('-f',help="Specify filename.")
        
"""
Reading the file containing domain names.
"""
with open(file_name) as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    
def do_request():
    for line in lines:
        try:
            req = requests.get(line, ssl_verify=False, timeout=5)
            if req.ok:
                print(line, end = ' ')
                print(200)
        except :
            pass

"""Connecting the domains from file using threads.
: Thread implementation
"""
threads = []
for i in range(no_threads):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(no_threads):
    threads[i].start()

for i in range(no_threads):
    threads[i].join()


exit(0)

