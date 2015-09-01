import csv
from os.path import expanduser
home = expanduser("~")

from collections import namedtuple

Person = namedtuple('person','name,sex,role,blackhair,glasses,basketball')
People = []

with open(home+'/Downloads/survey.csv', 'rb') as csvfile:

    datareader = csv.reader(csvfile)
    firstline = True
    for row in datareader:
        if firstline:
            firstline = False
        else:
            p = Person(row[1],row[2],row[3],row[12],row[11],row[13])
            People.append(p)

if __name__ == '__main__':
    print People

##spis student
##mentor
##prof

##glasses
##black hair
##basketball
##track or cross
##no sports
##no facebook
##played league
##uses iphone
##has siblings

'''college'''
##marshall
##warren
##revelle
##sixth
##erc
##muir
##not a student or mentor

'''mentors only'''
##second year
##third year
##fourth year
##fifth year
##sixth year
##seventh

'''students major'''
##cs
##ce
##undeclared
##other



