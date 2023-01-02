

numlist=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

def makeN(n, q):
  rev_base = ''
  while n > 0:
      n, mod = divmod(n, q)
      rev_base += str(numlist[mod])
  return rev_base[::-1] 


def solution(n, t, m, p):
  # n은 진법
  # t는 숫자의 갯수
  # m은 게임참가 인원
  # p는 튜브의 순서
  answer="0"
  realanswer=""
  for i in range(1,t*m):
    answer+=makeN(i,n)
  
  for i in range(p-1,t*m):
    if (i+1-p)%m==0:
      realanswer+=answer[i]
  return realanswer

print(solution(16,16,2,2))