from bs4 import BeautifulSoup
import urllib.request
import re
import time

URL = "https://www.betfair.com/sport/tennis" 
try:
    page = urllib.request.urlopen(URL)
except:
    print("An error occured.")

soup = BeautifulSoup(page, 'html.parser')

print("")
print("B̲E̲T̲ F̲A̲I̲R̲ S̲C̲R̲A̲P̲E̲R̲")
time.sleep(1)

title = soup.findAll("h1",{"class":"com-sh-title"})
arg=title[0]
print("==================================")
print(arg.text.strip())

inplay = soup.findAll("span",{"class":"section-header-title"})
arg=inplay[0]
print(arg.text.strip())
print("==================================")
print("")

def scan():

    gameno = 0
    argList = 0
    oddno1 = 0
    oddno2 = 0
    bad_chars = ['•']

    while True:

        PHstr = ": "

        odds1 = soup.findAll("li", {"class":"selection sel-0"})
        odds2 = soup.findAll("li", {"class":"selection sel-1"})

        try:
            odd1 = (odds1[oddno1])
        except IndexError:
            print("No more games found")
            print()
            print("Refreshing...")
            time.sleep(5)
            scan()

        try:
            odd2 = (odds2[oddno2])
        except IndexError:
            print("No more games found")
            print("Refreshing...")
            time.sleep(5)
            scan()

        print("GAME",gameno +1)
        print("")

        team1 = soup.findAll("span",{"class":"team-name"})
        try:
            arg=team1[argList]
        except IndexError:
            print("No more people playing")
            print("Refreshing...")
            time.sleep(5)
            scan()

        argList += 1
        team1C = (arg.text.strip())

        for i in bad_chars:
            team1C = team1C.replace(i, '')

        print(team1C.strip() + PHstr + odd1.text.strip())
        oddno1 += 1

        print("--VS--")

        team2 = soup.findAll("span",{"class":"team-name"})
        arg=team2[argList]
        argList += 1
        team2C = (arg.text.strip())

        for i in bad_chars:
            team2C = team2C.replace(i, '')

        print(team2C.strip() + PHstr + odd2.text.strip())
        oddno2 += 1

        gameno += 1
        print("=====================================================")

scan()

