


def solution(n):
  lst=0
  for i in range(2,n+1):
    flag=0
    for j in range(2,int(i**0.5)+1):
      if i%j==0:
        flag=1
        break
    if flag==0:
      lst+=1
  
  return lst

solution(10)