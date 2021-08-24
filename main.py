from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# Read URL + checkpoint from file
f = open("url.txt", "r")
c = open("checkpoint.txt", "r")
URL = f.readline().strip()
CHECKPOINT = c.readline().strip()
f.close()
c.close()

#Complete URL
FullURL = URL + CHECKPOINT
print(FullURL)

PAGE = urlopen(URL)

# soup = BeautifulSoup(PAGE, "html.parser")
# h4 = soup.find_all("h4")
# h4 = [i.text for i in h4]
# print(h4)
#
# f = open('2.csv', 'w')
# writer = csv.writer(f)
# for i in h4:
#     writer.writerow([i])
