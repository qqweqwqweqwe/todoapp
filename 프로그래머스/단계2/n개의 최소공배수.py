def L(num1,num2):
  start=1
  for i in range(1,int(min(num1,num2))+1):
    if num1%i==0 and num2%i==0:
      start=i
  
  return num1*num2/start



  return leastcommon

solution([2,6,8,14]	)