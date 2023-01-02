answer=0
count=-1
def solution(word):
  dictrio("",word)
  return answer
wordlist=['A','E','I','O','U']
def dictrio(words,search):
  global count
  global answer
  count+=1
  print(count)
  if words==search:
    answer=count
  for word in wordlist:
    if len(words)<=4:
      dictrio(words+word,search)



# 모든 재귀함수는 반복문으로 작성 가능하다 이건 팩트

"""
for alpha in list['a','b','c']:
  for alpha in list['a','b','c']:
    for alpha in list['a','b','c']:
      이런식으로 가능 굳이 재귀함수 쓸필요가 없었음
      


  

  """
print(solution("I"))

