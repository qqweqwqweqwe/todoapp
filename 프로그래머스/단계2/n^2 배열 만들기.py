def solution(n, left, right):
  answer = []
  standard=left//n
  for i in range(left, right+1):
    if standard!=i//n:
      standard=i//n
    if standard<=i%n:
      answer.append(standard+1)
    else:
      answer.append(n)
  return answer