import numpy
numofzero=0
numofone=0
a=numpy.array([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
def recursive(arr):
  global numofone
  global numofzero
  if numpy.all(arr==1):
    numofone+=1
    return
  elif numpy.all(arr==0):
    numofzero+=1
    return
  else:
    lenarr=len(arr)//2
    recursive(arr[0:lenarr,0:lenarr])
    recursive(arr[0:lenarr,lenarr:2*lenarr])
    recursive(arr[lenarr:lenarr*2,0:lenarr])
    recursive(arr[lenarr:lenarr*2,lenarr:lenarr*2])
def solution(arr):
  arr=numpy.array(arr)
  recursive(arr)
  answer = [numofzero,numofone]
  return answer
print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))








