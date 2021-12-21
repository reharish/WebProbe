import requests
from sys import argv
import re

#argv[1]

httpfile = open(argv[1],'rt')

for line in httpfile:
#    print(line)
    if re.search("^http*",line):
        req = requests.get(line)
    if req.ok:
        print(line)

httpfile.close()

