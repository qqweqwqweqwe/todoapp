from collections import Counter


def solution(s):
  answer=[]
  s=Counter(s.replace('{','').replace('}','').split(','))
  s=sorted(s.items(), key=lambda x:x[1], reverse=True)
  for i in s:
    answer.append(int(i[0]))
  return answer
  

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")