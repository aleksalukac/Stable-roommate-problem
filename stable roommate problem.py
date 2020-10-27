"""@author: Aleksa
Useful video reference
https://www.youtube.com/watch?v=9Lo7TFAkohE&ab_channel=JoyYeh
"""
lines = open('output.txt').read().splitlines()
lineNum = 0

def transformPreferenceMatrix():
    for i in range(n):
        prefMatrix.append([-1] * n)
        for j in range(n - 1):
            prefMatrix[i][preferenceMatrix[i][j]] = j

def removePair(i,j):
    if(j in preferenceMatrix[i]):
        preferenceMatrix[i].remove(j)
        preferenceMatrix[j].remove(i)

def isBetterOffer(sender, receiver):
    if(offers[receiver] == -1):
        return True
    if(prefMatrix[receiver][sender] < prefMatrix[receiver][offers[receiver]]):
        return True
    
    return False

def keepOnlyOffer(receiver, sender):
    returnVal = False
    if(sender in preferenceMatrix[receiver]):
        for j in reversed(range(len(preferenceMatrix[receiver]))):
            #atren1 = preferenceMatrix[i][j]
            #atren2 = offers[i]
            if(preferenceMatrix[receiver][j] != sender):
                removePair(receiver, preferenceMatrix[receiver][j])
                returnVal = True
            else:
                break
    
    return returnVal

def readMatrix():
    global lineNum
    global lines
    a=[] 
    for i in range(n):   
        a.append([int(j) for j in lines[lineNum].split()]) 
        lineNum += 1
    
    return a

def sortMatrix(inMatrix):
    temp_matrix = []
    for j in range(n):
        temp = [i[0] for i in sorted(enumerate(inMatrix[j]), key=lambda x:x[1])]
        
        for k in range(len(temp)):
            if(temp[k] >= j):
                temp[k] += 1
            
        temp_matrix.append(temp)
        
    return temp_matrix

prefMatrix = []

'''preferenceMatrix = [
    [1,2,4,5,3],
    [4,3,0,2,5],
    [4,5,1,0,3],
    [0,2,5,1,4],
    [0,1,3,5,2],
    [1,0,3,2,4]]'''
'''solution :0 -- [2]
1 -- [4]
2 -- [0]
3 -- [5]
4 -- [1]
5 -- [3]'''

'''preferenceMatrix = [
        [1,3,5,4,2],
        [4,2,5,3,0],
        [1,5,4,0,3],
        [2,0,5,1,4],
        [1,0,5,2,3],
        [0,3,4,2,1]]'''
'''solution:
0 -- [5]
1 -- [4]
2 -- [3]
3 -- [2]
4 -- [1]
5 -- [0]'''
    
'''
preferenceMatrix = [
        [2,3,1,5,4],
        [5,4,3,0,2],
        [1,3,4,0,5],
        [4,1,2,5,0],
        [2,0,1,3,5],
        [4,0,2,3,1]]


suitor_preferences = {
    "A": ["D", "B", "C"], "B": ["C", "A", "D"], "C": ["A", "B", "D"],
    "D": ["A", "B", "C"]
    }

'''

preferenceMatrix = [
    [3, 1, 2],
    [2, 0, 3],
    [0, 1, 3],
    [0, 1, 2]
    ]

n = len(preferenceMatrix)
    
offers = [-1] * n

if(__name__ == "__main__"):
    
    n = int(lines[lineNum])
    lineNum += 1
    
    offers = [-1] * n

    inMatrix = readMatrix()
    
    preferenceMatrix = sortMatrix(inMatrix)
    
    transformPreferenceMatrix()
    
    offerSenderOrder = list(range(n)) #should be linked list
    
    #step 1:
        
    while (len(offerSenderOrder) != 0):
        
        i = offerSenderOrder[0]
        offerSenderOrder.remove(i)
    
        for j in range(n - 1):
            
            if(j >= len(preferenceMatrix[i])):
               print("-1")
               exit()
           
            potentialPartner = preferenceMatrix[i][j]
            
            if(prefMatrix[i][potentialPartner] != -1):
                if(isBetterOffer(i, potentialPartner)):
                    
                    if(offers[potentialPartner] != -1):
                        offerSenderOrder.insert(0, offers[potentialPartner])
                        removePair(offers[potentialPartner], potentialPartner)
                        
                    offers[potentialPartner] = i 
                    break
    
    #step 1 over
    
    #step 2:
    
    for i in range(n):
        
        for j in reversed(range(len(preferenceMatrix[i]))):
            #atren1 = preferenceMatrix[i][j]
            #atren2 = offers[i]
            if(preferenceMatrix[i][j] != offers[i]):
                removePair(i, preferenceMatrix[i][j])
            else:
                break
            
    #step 2 over
    
    #step 3:
    
    finishedNode = [False] * n
    
    while(True):
        
        shouldDoubleCheck = True
        """
        while(shouldDoubleCheck):
            shouldDoubleCheck = False
            for i in range(n):
                if(len(preferenceMatrix[i]) == 1 and not finishedNode[i]):
                        shouldDoubleCheck = shouldDoubleCheck or keepOnlyOffer(preferenceMatrix[i][0], i)
                        finishedNode[i] = True
                        """
        q_list = [] # q[i] is the second preference of p[i]
        p_list = [] # p[i] is the last preference of q[i-1]
        for i in range(len(preferenceMatrix)):
            if(len(preferenceMatrix[i]) == 0):
                print("-1")
                exit()
                
            if(len(preferenceMatrix[i]) > 1):
                p_list.append(i)
                break
        
        if(len(p_list) == 0):
            break
        
        while(True):
            if(len(preferenceMatrix[p_list[-1]]) <= 1):
                print("-1")
                exit()
                
            q_list.append(preferenceMatrix[p_list[-1]][1])
            p_list.append(preferenceMatrix[q_list[-1]][-1])
            
           #if(p_list[-1] == p_list[0]):
            if(p_list[-1] in p_list[:-1]):
                for i in range(p_list.index(p_list[-1]), len(q_list)):
                    #print(p_list[i+1],q_list[i])
                    removePair(p_list[i+1], q_list[i])
                    
                for i in range(n):
                    if(len(preferenceMatrix[i]) == 0):
                        print("-1")
                        exit()
                    keepOnlyOffer(preferenceMatrix[i][0], i)
                
                break
                
    for i in range(len(offers)):
        
        print(str(preferenceMatrix[i][0] + 1))
