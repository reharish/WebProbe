import threading
import requests
import argparse

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
    print(url)
    response = requests.get(url, verify=False, timeout=5)
    if response.ok:
        print(url)
        
def process_file(fname, t):
    n_threads = []
    fp = open(fname,'rt')
    while True:
        line=fp.readline().strip()
        if not line:
            break            
        request = threading.Thread(target=do_request, args=(line,))
        if len(n_threads) == t:
            while True:
                for i in n_threads:
                    if not i.is_alive():
                        i = request
                        break
        else:
             n_threads.append(request)
             request.start()
             




if __name__=="__main__":
    process_file(args.filename, args.thread)
