from curses.ascii import NL


def solution(n):
  answer=0
  n=list(str(n))
  for i in n:
    answer+=int(i)
  return answer

solution(123)