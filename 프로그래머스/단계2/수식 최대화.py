from itertools import permutations



def calculate(num1, num2, op):
  if op=='+':
    return str(int(num1)+int(num2))
  elif op=='*':
    return str(int(num1)*int(num2))
  elif op=='-':
    return str(int(num1)-int(num2))

def prioritycal(op,prioritylist:tuple):
  return prioritylist.index(op)
  



def solution(expression:str):
  answer=0
  expression=expression+' '
  temp=''
  array=[]
  for i in expression:
    if i.isdigit():
      temp+=i
    else:
      array.append(temp)
      array.append(i)
      temp=''
  array=array[0:-1]


  op=['*','+','-']
  prioritys=list(permutations(op))
  for priority in prioritys:
    stack=[]
    result=[]
    for i in array:
      if i.isdigit():
        result.append(i)
      else:
        if len(stack)==0:
          stack.append(i)
        else:
          while len(stack)>=1 and prioritycal(stack[-1],priority)>= prioritycal(i,priority):
            result.append(stack.pop())  
          stack.append(i)
    while len(stack)!=0:
      result.append(stack.pop())
    
    print(result, priority)

    
    for i in result:
      if i.isdigit():
        stack.append(i)
      else:
        second=stack.pop()
        first=stack.pop()
        stack.append(calculate(first,second,i))
    
    if answer<abs(int(stack[0])):
      answer=abs(int(stack[0]))
    
  return answer


print(solution("100-200*300-500+20"))