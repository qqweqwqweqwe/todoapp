from itertools import combinations
from operator import truediv


def solution(relation):
  answer=0
  testlen=len(relation)
  keylist=[0,1,2,3]
  tuplelist=[]
  for i in range(1,len(keylist)+1):
    tuplelist+=list(combinations(keylist,i))

  while 
  for tpl in tuplelist:
    testset=set()
    for rel in relation:
      teststr=""
      dataset=set()
      for i in tpl:
        teststr+=rel[i]
      testset.add(teststr)
    if len(testset)==testlen:
      templist=[]
      answer+=1
      for tppl in tuplelist:
        for i in tpl:
          break
        templist.append(tppl)
      tuplelist=templist
      break
      
        
        

            


      
      

  
solution(1)