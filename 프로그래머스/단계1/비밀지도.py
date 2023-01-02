
def solution(n, arr1,arr2):

  for i in range(n):
    arr1[i]=(bin(arr1[i]|arr2[i]))[2:n+2].rjust(n,'0')
  
    
  print(arr1)
  answer=[]

  
  for i in range(n):
    answer.append(arr1[i].replace('1','#').replace('0',' '))


  return answer

solution(6,[46, 33, 33 ,22, 31, 50]
,[27 ,56, 19, 14, 14, 10])