def solution(brown, yellow):
  for i in range(1,int(yellow**0.5)+1):
    if yellow%i==0:
      if (i+yellow//i)*2+4==brown:
        return list([yellow//i+2,i+2])