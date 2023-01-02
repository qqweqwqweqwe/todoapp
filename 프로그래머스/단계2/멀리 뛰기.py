def solution(n):
  answer=[0]*2001
  answer[1],answer[2]=1,2
  for i in range(3,2001):
    answer[i]=answer[i-1]+answer[i-2]
  return answer[n]%1234567


print(solution(2000))