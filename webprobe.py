import threading
import requests
import argparse
from time import sleep

"""ArgParse for CLI input"""

parser=argparse.ArgumentParser(description='WebProbe V0.1')
parser.add_argument('-f','--filename',type=str,required=True,help="Specify filename.")
parser.add_argument('-t','--threads',type=int,const=5,nargs='?',help="Specify No.of threads to spawn (default = 5)")

args = parser.parse_args()

"""Supressing warning caused by requests"""

requests.packages.urllib3.disable_warnings()

def do_request(url):
    """ Post request to the site
    print the url to console if response is 200
    """
    if not url: return
    try:
        response = requests.get(url, verify=False, allow_redirects=False, timeout=1)
        print(url) #if response.ok else print(f"response: {response.status_code} url: {url}")
    except Exception as e:
        pass


def process_file(fname, t):
    """ Thread Implementation """
    fp = open(fname,'rt')
    arr = list(map(lambda a : a.strip(), fp.readlines()))
    for each in arr:
        req = threading.Thread(target=do_request, args=(each,))
        #print(threading.active_count())
        while threading.active_count() >=t:
            sleep(0.1)
        # Needs to be changed
        req.start()
    fp.close()

if __name__=="__main__":
    try:
        if args.threads == None:
            threads_c=5
        else:
            threads_c=args.threads
        #print(15*"="+"\nFile Name : {}\nThread Count : {}\n".format(args.filename,threads_c)+15*"="+"\n")
        process_file(args.filename, threads_c)
    except Exception as err:
        print("\33[031mError !!\33[0m\n \n{}".format(err))
