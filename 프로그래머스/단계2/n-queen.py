ans=0
def promising(x,place):
  for i in range(x):
    if place[x]==place[i] or abs(place[x]-place[i])==abs(x-i):
      return False
  return True

def nqueen(x,n,place):
  global ans
  if x==n:
    ans+=1
    return
  for i in range(n):
    place[x]=i
    if promising(x,place):
      nqueen(x+1,n,place)


def solution(n):
  place=[0]*n
  nqueen(0,n,place)



  return ans

  

    

