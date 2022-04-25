import threading
import requests
import argparse
from time import sleep
"""
ArgParse to getting input
"""
parser=argparse.ArgumentParser(description='WebProber V1.0')
parser.add_argument('-f','--filename',type=str,required=True,help="Specify filename.")
parser.add_argument('-t','--thread',type=int,const=5,nargs='?',help="Specify No.of threads to spawn (default = 5)")

args = parser.parse_args()

"""
Supressing warning caused by requests
"""
requests.packages.urllib3.disable_warnings()

def do_request(url):
    if not url: return
    try:
        response = requests.get(url, verify=False, allow_redirects=False, timeout=5)
        print(url) if response.ok else print(f"response: {response.status_code} url: {url}")
    except Exception as e:
        pass
        

def process_file(fname, t=5):
    fp = open(fname,'rt')
    arr = list(map(lambda a : a.strip(), fp.readlines()))
    for each in arr:
        req = threading.Thread(target=do_request, args=(each,))
        while threading.active_count() >= t:
            sleep(1) #every one sec we are checking thread count
        req.start(), req.join()


if __name__=="__main__":
    process_file(args.filename, args.thread)
