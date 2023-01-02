def solution(n, works):
  total=0
  answer=0
  for i in works:
    total+=i
  total-=n
  if total<=0:
    return answer
  
  else:
    standard=0
    if total%n==0:
      standard=total//n
    else:
      standard=int(total/n)+1

      
      
    for i in works:
      if n==0:
        break
      if i>standard:
        j=max(standard,i-n)
        answer+=j**2
        n-=i-j
      else:
        answer+=i**2
        

  return answer

print(solution(4,[4, 3, 3]))