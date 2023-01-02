def SORT(num):
  



def solution(numbers:list):
  answer = ''

  numbers.sort(key=lambda x : str(x)[-1], reverse= True)
  for number in numbers:
    answer=answer+str(number)
  return answer

print(solution([3, 30, 34, 5, 9]))