

def solution(dartResult:str):
  answer=[]
  num=0
  count=0
  dartResult=dartResult.replace('10','A')
  for dart in dartResult:
    if dart.isdigit():
      answer.append(num)
      num=int(dart)
      count+=1
    elif dart=='A':
      answer.append(num)
      num=10
      count+=1
    
    elif dart=='D':
      num=num**2
    elif dart=='T':
      num=num**3
    elif dart=='*':
      num=num*2
      answer[count-1]=answer[count-1]*2
    elif dart=='#':
      num=num*-1
  answer.append(num)
  total=0
  for a in answer:
    total+=a
  return total

solution("1D2S#10S")

      


    


