def solution(s:str):
  words=list(s.split(' '))
  answer=''
  for word in words:
    answer=answer+word.capitalize+' '
  answer=answer[:-1]
  return answer