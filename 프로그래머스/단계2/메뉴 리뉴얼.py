from itertools import combinations
from typing import Counter
def solution(orders, course):
  answerlist=[]
  for i in course:
    countlist=[]
    for order in orders:
      order=list(order)
      order.sort()
      countlist+=list(combinations(order,i))
    countlist=Counter(countlist).most_common()
    if countlist:
      maxval=countlist[0][1]
      for i in countlist:
        answer=""
        if i[1]==maxval and i[1]>=2:
          for j in i[0]:
            answer+=j
          answerlist.append(answer)
        else:
          break
  answerlist.sort()
  return answerlist
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))