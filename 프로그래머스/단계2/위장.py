from itertools import combinations
def solution(clothes):
  cloth_dict={}
  for cloth in clothes:
    if cloth[1] not in cloth_dict.keys():
      cloth_dict[cloth[1]]=[]
    cloth_dict[cloth[1]].append(cloth[0])
  count=1
  for i in cloth_dict.keys():
    count=count*(1+len(cloth_dict[i]))
  return count-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	)