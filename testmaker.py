import json
from random import randint

""" Minor variable changes for testing purposes """
preset=25  #number of nodes
openess=0  #percentage of the connections that are from outside the closed system [where 0 = closed system with no outside references, 50 = half of the connections are openended nodes with no info in the database, and 100 is an error coz of the use of infinite as limit]
max_connections = 20    #the maximum connections a node could have, the number of connections is decided between 1 and this variable
pre_notation="n_"    # to display all nodes as just string of numbers, use "". "n_" setting shows the nodes as "n_123" instead of "123"
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

gen(preset)

data = json.dumps(data,indent=4)
with open("testdata.json","w+") as f:
    f.write(data)