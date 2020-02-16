from urllib.request import urlopen
from sys import argv, stdout
from re import search, I

try:
    if len(argv) < 2:
        print("Usage: webget URL\n")
        exit(0)

    url = argv[1]
    web = urlopen(url)
    mediatype = web.getheader("content-type")
    data = web.read()
    web.close()

    if mediatype.startswith("text/"):
        match = search(r'charset\s*=\s*(.*)', mediatype, flags=I)
        charset = match.group(1) if match else "utf-8"
        text = data.decode(charset)
        print(text, end="")
    else:
        stdout.buffer.write(data)

except Exception as ex:
    print(ex.__class__.__name__, ":", ex)
