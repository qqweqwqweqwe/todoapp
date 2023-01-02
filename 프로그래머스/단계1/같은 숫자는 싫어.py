def solution(arr):
  brr=[]
  brr.append(arr[0])
  for i in arr:
    if brr[-1]!=i:
      brr.append(i)

  return brr


# 리스트 슬라이싱은 빈 배열일때도 가능
