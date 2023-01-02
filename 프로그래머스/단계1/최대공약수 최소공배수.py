def solution(n, m):
  answer = [0,0]
  i=1
  while i<=min(n,m):
    if m%i==0 and n%i==0:
      answer[0]=i
    i+=1
  answer[1]=(n*m)//answer[0]
  return answer