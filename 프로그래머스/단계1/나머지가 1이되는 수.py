def solution(n):
  for i in range(n-2, 0, -1):
    if (n-1)%i==0:
      return (n-1)//i
    



print(solution(10))