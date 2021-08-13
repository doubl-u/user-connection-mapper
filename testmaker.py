import json
from random import randint
from typing import Counter

""" Minor variable changes for testing purposes """
preset=25  #number of nodes
openess=0  #percentage of the connections that are from outside the closed system [where 0 = closed system with no outside references, 50 = half of the connections are openended nodes with no info in the database, and 100 is an error coz of the use of infinite as limit]
max_connections = 20    #the maximum connections a node could have, the number of connections is decided between 1 and this variable
pre_notation="n_"    # to display all nodes as just string of numbers, use "". "n_" setting shows the nodes as "n_123" instead of "123"
code_digits=10      #This changes the number of place values the exported codes assigned to the names will have
""" Any changes made below needs to be tested before pushing to repository """

data = []
def gen(n):
    for i in range(1,n+1):  #creates a node for every number from 1 to n, as i
        r = []  #The connections of every node
        for j in range(randint(0,max_connections)):  #number of connections the node is randomized
            op = openess/100    #convertion from % to fraction
            limit=int(n+(op*n)/(1-op))  #the derived algebraic formula to find the limit that needs to be set [n+n*ratio/(1-ratio), where ratio is op^] 
            r2 = str(randint(1,limit))
            if r2 not in r and r2 != str(i):    #checks if the connection isnt already established, or that it is not connected to itself
                r.append(pre_notation+r2)
            else:j-=1   #to re-run the connection creation if the loop was passed
        data.append({"node":pre_notation+str(i),"connections":r})

def genCode(c,length):
    for i in range(length):
        while True:
            r = randint(10**code_digits,10**(code_digits+1))
            print(f"r={r}")
            if r in c:pass
            else:
                c.append(r)
                break
    return c

gen(preset)
data2={"nodes":[],"links":[]}
codes=genCode([],len(data))

def gen2_1(l,tar):
    #print(f"{l} <")
    for i in l:
        if i["name"]==tar:return i["id"]

def gen2(d):
    Counter=0
    for i in d:
        n = i["node"]
        data2["nodes"].append({"name":n,"id":codes[Counter]})
        Counter+=1
    Counter=0
    for i in d:
        for j in i["connections"]:
            data2["links"].append({"source":codes[Counter],"target":gen2_1(data2["nodes"],j)})
        Counter+=1

gen2(data)

data = json.dumps(data,indent=4)
data2 = json.dumps(data2,indent=4)
with open("testdata1.json","w+") as f:f.write(data)
with open("testdata2.json","w+") as f:f.write(data2)