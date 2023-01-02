def solution(n):
  
  fisrt=1
  second=2

  for i in range(3,n+1):
    fisrt,second=second,fisrt+second
    

  
  return second%1000000007

  


print(solution(100))