from bs4 import BeautifulSoup
from time import sleep
from urllib.request import urlopen
from funcs import *

# Read URL + checkpoint from file
f = open("url.txt", "r")
c = open("checkpoint.txt", "r")
URL = f.readline().strip()
CHECKPOINT = int(c.readline().strip())
f.close()
c.close()

data = []
checkpoint = []
CHECKPOINT , PAGE = skip(URL , CHECKPOINT)
# print(CHECKPOINT)

x = 0

while True:
# sleep(0.05)
    x += 1
    if x == 10:
        x = 0
        writeToFile(data , CHECKPOINT)
        data = []
        print("50 done")
    try:
        print(CHECKPOINT)
        FullURL = URL + str(CHECKPOINT)
        # print(FullURL)
        PAGE = urlopen(FullURL)
        soup = BeautifulSoup(PAGE, "html.parser")
        td = soup.find_all("td")
        td = [i.text.strip().replace("," , ":") for i in td]
        data.append(td)
        checkpoint.append(CHECKPOINT)
        CHECKPOINT += 1
    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
        break
    except Exception as e:
        print(e)
        if e.code == 404:
            CHECKPOINT += 1
        else:
            break

writeToFile(data , CHECKPOINT)