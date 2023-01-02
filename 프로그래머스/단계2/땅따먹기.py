def solution(land):
  for a in range(1,len(land)):
    for i in range(4):
      maxnum=0
      for j in range(4):
        if i!=j:
          maxnum=max(maxnum,land[a-1][j])
      land[a][i]+=maxnum
  return max(land[len(land)-1])