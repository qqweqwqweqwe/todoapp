def divide(numstr):
  total=[]
  curstr=""
  for num in numstr:
    if num=='0':
      if len(curstr)>1:
        total.append(curstr)
      curstr=''
    else:
      curstr+=num
  total.append(curstr)
  return total

def isitprime(num):
  if num<2:
    return False
  for i in range(2, int(num**1/2)+1):
    if num%i==0:
      return False
  return True

def solution(n, k):
  answer=0
  rev_base = ''
  while n > 0:
    n, mod = divmod(n, k)
    rev_base += str(mod)
  numstr=rev_base[::-1] 
  
  numlist=divide(numstr)

  for num in numlist:
    if isitprime(int(num)):
      answer+=1
  return answer

solution(437674,3)


    


