from typing import Counter


def solution(n):
  n=Counter(str(n))
  answer = ''
  n=sorted(n.items(), reverse=True)
  print(n)
  for i in n:
    answer+=i[0]*i[1]
  return int(answer)

print(solution(123131123))


# join 함수랑 list(str(n)) 이거 기억하기
