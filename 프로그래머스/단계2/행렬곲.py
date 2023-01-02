

import numpy


def solution(arr1, arr2):
  arr1=numpy.array(arr1)
  arr2=numpy.array(arr2)

  return (arr1@arr2).tolist()


print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]	))

