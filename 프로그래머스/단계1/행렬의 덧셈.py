def solution(arr1, arr2):
    for i in range(len(arr1)):
      for j in range(len(arr1[0])):
        arr2[i][j]+=arr1[i][j]
                  
    answer = arr2
    return answer