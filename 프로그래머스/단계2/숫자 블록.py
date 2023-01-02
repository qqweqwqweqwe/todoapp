def whatisnum(num):
  if num==1:
    return 0
  maxnum=1
  for i in range(2, int(num**1/2)+1):
    if num%i==0 and num%i<=10000000:
      return num//i
  return maxnum




def solution(begin, end):
  answer=[]
  for i in range(begin, end+1):
    answer.append(whatisnum(i))
  return answer


# 반복문으로 가능한것은 최대한 반복문으로
# 실행시간 차이가 존나 심함
