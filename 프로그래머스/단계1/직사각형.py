def solution(sizes):
  maxlist=[]
  minlist=[]
  for size in sizes:
    maxlist.append(max(size))
    minlist.append(min(size))
  return max(maxlist)*max(minlist)