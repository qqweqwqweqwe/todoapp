def solution(x):
  remain=0
  y=x
  while y:
    remain+=y%10
    y=y//10
  return x%remain==0