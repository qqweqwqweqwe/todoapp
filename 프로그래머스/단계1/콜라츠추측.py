

def solution(num):
  num_count=0
  while num>1:
    if num%2==0:
      num=num//2
      num_count+=1
    else:
      num=num*3+1
      num_count+=1
    if num_count==500:
      return -1
  
  return num_count

    
