import csv
import sys
import os
import csv
import collections
import pandas as pd
from math import*
from decimal import Decimal


#os.remove('')
#---Code to do all the formatting---#

#---Code to append a Header to the result-set!---#
def defineHeader(name):
    with open('sorted.csv',newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('sorted.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow([name,'Articles'])
        w.writerows(data)
    return

#---Code to merge both CSV Files---#
def mergeCSV(filename):
    with open('artlist.csv', 'r') as book1:
        with open(filename, 'r') as book2:
            reader1 = csv.reader(book1, delimiter=',')
            reader2 = csv.reader(book2, delimiter=',')

            both = []
       
            for row1, row2 in zip(reader1, reader2):
                row2.append(row1[0])
                both.append(row2)

            with open('final.csv', 'w') as output:
                writer = csv.writer(output, delimiter=',')
           
                writer.writerows(both)
    #sortResult('final.csv')
            
    return

#---Code to Swap the Columns in the CSV---#
def swapCols():
    with open('sorted.csv', 'r') as infile, open('EuclideanDistance.csv', 'a') as outfile:
        # output dict needs a list for new column ordering
        fieldnames = ['Articles','Euclidean Distance']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        # reorder the header first
        writer.writeheader()
        for row in csv.DictReader(infile):
            # writes the reordered rows to the new file
            writer.writerow(row)
    os.remove('eudist.csv')
    os.remove('final.csv')
    os.remove('sorted.csv')
    return

#---Code to Sort the Result-Set---#
def sortResult(filename):
    with open(filename) as f:
        d = dict(filter(None, csv.reader(f)))

    od = sorted(d.items(), key = lambda items:items[0])


    with open('sorted.csv','w') as f:
        writer = csv.writer(f)
        writer.writerows(od)
    return

#---Euclidean Distance---#   
def euclidean_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
fi = open("testdata.csv")
with open('eudist.csv', 'w') as fo:
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(euclidean_distance(v[x-1],v[x]),file=fo)
#mergeCSV('eudist.csv')


mergeCSV('eudist.csv')
sortResult('final.csv')
defineHeader('Euclidean Distance')
swapCols()

'''

#---Jaccard Distance---#
def jaccard_similarity(x,y): 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)
fi = open("testdata.csv")
with open('JaccardDistance.txt', 'w') as fo:    
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(jaccard_similarity(v[x-1],v[x]),file=fo)

#---Cosine Distance---#
def square_rooted(x): 
    return round(sqrt(sum([a*a for a in x])),3)
def cosine_similarity(x,y): 
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)
fi = open("testdata.csv")
with open('CosineDistance.txt', 'w') as fo:    
    v =[]
    for x, line in enumerate(fi):        
        v.append([int(z) for z in (line.split(',')) if z])
        print(cosine_similarity(v[x-1],v[x]),file=fo)
'''
