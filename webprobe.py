import requests
from sys import argv
import re

arguments = ["--thread", "-t", "-o", "--output"]

if argv[1] in arguments:
    if argv[1] == "--thread" or argv[1] == "-t":
      if int(argv[2]) < 120 :
          thread = int(argv[2])
      else:
          print("Invalid Thread")

def TheMain():
    httpfile = open(argv[1],'rt')
    for line in httpfile:
        line = line.split('\n');
        line = line[0]
        if re.search("^http*",line):
            req = requests.get(line)
        if req.ok:
            print(200)
            print(line)
    httpfile.close()

