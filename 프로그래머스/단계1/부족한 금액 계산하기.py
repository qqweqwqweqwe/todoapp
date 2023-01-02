def solution(price, money, count):
  answer=0
  for c in range(1,count+1):
    answer+=c*price
  if answer-money<0:
    return 0
  return answer-money