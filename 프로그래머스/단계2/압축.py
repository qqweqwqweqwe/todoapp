

def solution(msgs):
  alphabetlist=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  start=0
  answer=[]
  for j in range(len(msgs)):
    cur=""
    for i in range(start,len(msgs)):
      bef=cur
      cur+=msgs[i]
      if cur in alphabetlist:
        if i==len(msgs)-1:
          answer.append(alphabetlist.index(cur)+1)
          return answer
        continue
      else:
        alphabetlist.append(cur)
        answer.append(alphabetlist.index(bef)+1)
        start=i
        break

solution("TOBEORNOTTOBEORTOBEORNOT")


    
