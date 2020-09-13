# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:50:48 2020

@author: Aleksa

Useful video reference
https://www.youtube.com/watch?v=9Lo7TFAkohE&ab_channel=JoyYeh
"""

def transformPreferenceMatrix():
    for i in range(n):
        prefMatrix.append([-1] * n)
        for j in range(n - 1):
            prefMatrix[i][preferenceMatrix[i][j]] = j

def removePair(i,j):
    preferenceMatrix[i].remove(j)
    preferenceMatrix[j].remove(i)

def isBetterOffer(sender, receiver):
    if(offers[receiver] == -1):
        return True
    if(prefMatrix[receiver][sender] < prefMatrix[receiver][offers[receiver]]):
        return True
    
    return False
    

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

preferenceMatrix = [
        [1,3,5,4,2],
        [4,2,5,3,0],
        [1,5,4,0,3],
        [2,0,5,1,4],
        [1,0,5,2,3],
        [0,3,4,2,1]]
'''solution:
0 -- [5]
1 -- [4]
2 -- [3]
3 -- [2]
4 -- [1]
5 -- [0]'''
    
n = len(preferenceMatrix)
    
offers = [-1] * n


if(__name__ == "__main__"):
    
    transformPreferenceMatrix()
    
    offerSenderOrder = list(range(n)) #should be linked list
    
    #step 1:
        
    while (len(offerSenderOrder) != 0):
        
        i = offerSenderOrder[0]
        offerSenderOrder.remove(i)
    
        for j in range(n - 1):
            
            if(j >= len(preferenceMatrix[i])):
               print("Not possible")
               quit()
           
            potentialPartner = preferenceMatrix[i][j]
            
            if(prefMatrix[i][potentialPartner] != -1):
                if(isBetterOffer(i, potentialPartner)):
                    
                    if(offers[potentialPartner] != -1):
                        offerSenderOrder.insert(0, offers[potentialPartner])
                        preferenceMatrix[offers[potentialPartner]].pop(0)
                        preferenceMatrix[potentialPartner].remove(offers[potentialPartner])
                    offers[potentialPartner] = i 
                    break
    
    #step 1 over
    
    #step 2:
    
    for i in range(n):
        
        for j in reversed(range(len(preferenceMatrix[i]))):
            #atren1 = preferenceMatrix[i][j]
            #atren2 = offers[i]
            if(preferenceMatrix[i][j] != offers[i]):
                preferenceMatrix[preferenceMatrix[i][j]].remove(i)
                preferenceMatrix[i].pop()
            else:
                break
            
    #step 2 over
    
    #step 3:
    
    while(True):
        
        q_list = [] # q[i] is the second preference of p[i]
        p_list = [] # p[i] is the last preference of q[i-1]
        for i in range(len(preferenceMatrix)):
            if(len(preferenceMatrix[i]) == 0):
                print("Not possible")
                quit()
                
            if(len(preferenceMatrix[i]) > 1):
                p_list.append(i)
                break
        
        if(len(p_list) == 0):
            break
        
        while(True):
            if(len(preferenceMatrix[p_list[-1]]) <= 1):
                print("Not possible")
                quit()
                
            q_list.append(preferenceMatrix[p_list[-1]][1])
            p_list.append(preferenceMatrix[q_list[-1]][-1])
            
            if(p_list[-1] == p_list[0]):
                for i in range(len(q_list)):
                    removePair(p_list[i+1],q_list [i])
                
                break
            
    printed = []
    
    for i in range(len(offers)):
        
        print(str(i) + " -- " + str(preferenceMatrix[i]))
        #if(i not in printed):
          #  print(str(i) + " -- " + str(offers[i]))
            #printed.append(i)
            #printed.append(offers[i])
    
    
    
    
    
    
    