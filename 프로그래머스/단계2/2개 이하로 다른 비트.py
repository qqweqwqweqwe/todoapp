def solution(numbers):
  answer=[]
  for number in numbers:
    number=bin(number)[2:]
    if '0' not in number:
      number='0'+number
    start=len(number)-1
    while number[start]=='1':
      start-=1
    number=list(number)
    if start==len(number)-1:
      number[start]='1'
      number="".join(number)
    else:
      number[start]='1'
      number[start+1]='0'
      number="".join(number)
    answer.append(int('0b'+number,2))

  return answer 

    
