def solution(numbers, k):
  s=""
  start=0
  temp=0
  stand=0
  while len(s)<len(numbers)-k:
    stand=numbers[temp]
    for i in range(temp, min(start+k+1,len(numbers))):
      if numbers[i]=='9':
        temp=i
        stand=numbers[i]
        break
      if numbers[i]>stand:
        temp=i
        stand=numbers[i]
    s+=str(stand)
    start+=1
    temp+=1
  return s
  
print(solution("4177252841",4))