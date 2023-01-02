def solution(array:list, commands):
  answer = []
  for command in commands:
    a=array.copy()
    a=sorted(a[command[0]-1:command[1]])
    answer.append(a[command[2]-1])
  return answer


print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 람다 함수 공부
