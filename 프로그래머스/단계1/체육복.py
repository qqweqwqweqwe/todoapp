

def solution(n, lost, reserve):
  n=[1]*n
  for l in lost:
    n[l-1]-=1
  for r in reserve:
    n[r-1]+=1
  
  numoflost=len(n)-n.count(0)

  for i in range(len(n)):
    if n[i]==0 and i-1>=0 and n[i-1]==2:
      n[i]=1
      n[i-1]=1
      numoflost+=1
      continue
    if i+1<=len(n)-1 and n[i+1]==2 and n[i]==0 :
      n[i]=1
      n[i+1]=1
      numoflost+=1
      continue

  answer = numoflost
  return answer

  # 두 갈래로 나눠서 생각하기
  