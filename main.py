from bs4 import BeautifulSoup
import csv
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

while True:
  # sleep(0.05)
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
      CHECKPOINT += 1

c = open("checkpoint.txt", "w")
c.write(str(CHECKPOINT))

f = open('1.csv', 'a')
writer = csv.writer(f)
for i in data:
    writer.writerow(i)
