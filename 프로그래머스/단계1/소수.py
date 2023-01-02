from itertools import combinations
def primenumber(x):
  for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
    if x % i == 0:		
      return False
  return True				# 전부 나눠떨어지지 않으면 True
def solution(nums):
  answer = 0
  combs=list(combinations(nums,3))
  for comb in combs:
    total=sum(comb)
    if primenumber(total):
      answer+=1
  return answer