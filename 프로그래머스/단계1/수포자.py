def solution(answers):
  one=[1,2,3,4,5]
  two=[2, 1, 2, 3, 2, 4, 2, 5]
  three=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  corrent=[0,0,0]
  answer = []
  for i in range(len(answers)):
    if answers[i]==one[i%len(one)]:
      corrent[0]+=1
    if answers[i]==two[i%len(two)]:
      corrent[1]+=1
    if answers[i]==three[i%len(three)]:
      corrent[2]+=1
  for i in range(len(corrent)):
    if corrent[i]==max(corrent):
      answer.append(i+1)
  
  answer.sort()
  return answer

# enumerate 는 인덱스랑 값을 같이 묶어주는듯?


print(solution([1,2,3,4,5]))