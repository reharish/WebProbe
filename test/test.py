import argparse
import threading

parser=argparse.ArgumentParser(description='WebProber V1.0')
parser.add_argument('-f','--filename',type=str,required=True,help="Specify filename.")
parser.add_argument('-t','--thread',type=int,const=5,nargs='?',help="Specify No.of threads to spawn (default = 5)")

args = parser.parse_args()
urlfile=open(args.filename,'rt')

# test

for i in range(5):
    line=urlfile.readline()
    print(line)
    
