from functools import cmp_to_key


def bignum(num1,num2):
  num1=str(num1)
  num2=str(num2)
  while len(num1)!=len(num2):
    if len(num1)>len(num2):
      num2+=num2[-1]
    else:
      num1+=num1[-1]
  if num1>=num2:
    return -1
  else:
    return 1

def solution(numbers):
  answer=''
  numbers=sorted(numbers, key=cmp_to_key(bignum))
  for number in numbers:
    answer+=str(number)
  return answer

print(solution([1, 11, 110, 1110]))