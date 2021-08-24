from time import sleep
from urllib.request import urlopen

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
