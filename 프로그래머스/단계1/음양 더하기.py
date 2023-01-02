def solution(absolutes, signs):
  num=0
  for i in range(len(absolutes)):
    if signs[i]==True:
      num+=absolutes[i]
    else:
      num-=absolutes[i]
  answer = num
  return answer



# zip 함수 사용해서 풀어보자
