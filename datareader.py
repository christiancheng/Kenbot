import csv
from os.path import expanduser
home = expanduser("~")

from collections import namedtuple

Person = namedtuple('person','name,sex,student,blackhair,glasses,basketball,track, \
                    noSports,noFacebook,playedLeague,usesiPhone,haveSiblings, \
                    marshall,warren,revelle,sixth,erc,muir')
People = []

with open("survey.csv", 'rb') as csvfile:

    datareader = csv.reader(csvfile)
    firstline = True
    for row in datareader:
        if firstline: #ignores the first row of the csv
            firstline = False
        else:
            p = Person(row[1],row[2],row[3],row[12],row[11],row[13],row[14], \
                       row[15],row[16],row[17],row[18],row[19],row[20],row[21], \
                       row[22],row[23],row[24],row[25])
            People.append(p)

if __name__ == '__main__':
    print People





