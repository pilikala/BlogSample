from urllib.request import urlopen
from sys import argv

try:
    if len(argv) < 2:
        print("Usage: webhead URL\n")
        exit(0)

    url = argv[1]
    web = urlopen(url)
    headers = web.getheaders()
    web.close()

    for (key, val) in headers:
        print(key, ":", val)

except Exception as ex:
    print(ex.__class__.__name__, ":", ex)
