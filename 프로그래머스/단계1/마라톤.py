def solution(participant, completion):
  dict={}
  for par in participant:
    dict[par]=0
  
  for part in participant:
    dict[part]+=1
  
  for comp in completion:
    dict[comp]-=1
  
  for i in dict.keys():
    if dict[i]==1:
      return i
    

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))


#counter 함수 써서 다시해보자 하 ㅋㅋ 시발 파이썬의 간결함이란 counter 객체는 뺴기 연산이 가능하다
