from time import sleep
from urllib.request import urlopen
import csv

def skip(URL , CHECKPOINT):
  while True:
      sleep(0.05)
      try:
          #Complete URL
          FullURL = URL + str(CHECKPOINT)
          # print(FullURL)
          PAGE = urlopen(FullURL)
          break
      except Exception as e:
          print(e)
          CHECKPOINT += 1
  return(CHECKPOINT , PAGE)

def writeToFile(data,CHECKPOINT):
    c = open("checkpoint.txt", "w")
    c.write(str(CHECKPOINT))

    f = open('1.csv', 'a')
    writer = csv.writer(f)
    for i in data:
        writer.writerow(i)
