from urllib.request import urlopen
from sys import argv, stdout
from re import search, I

try:
    if (len(argv) >= 3) and (argv[1] == "-b"):
        url = argv[2]
        mode = "bin"
    elif len(argv) >= 2:
        url = argv[1]
        mode = "text"
    else:
        print("Usage: webget [-b] URL")
        print("  -b : force binary mode")
        exit(0)

    web = urlopen(url)
    mediatype = web.getheader("content-type")
    data = web.read()
    web.close()

    if mediatype.startswith("text/") and (mode == "text"):
        match = search(r'charset\s*=\s*(.*)', mediatype, flags=I)
        charset = match.group(1) if match else "utf-8"
        text = data.decode(charset, errors="ignore")
        print(text, end="")
    else:
        stdout.buffer.write(data)

except Exception as ex:
    print(ex.__class__.__name__, ":", ex)
