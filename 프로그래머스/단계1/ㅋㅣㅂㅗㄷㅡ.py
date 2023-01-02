from math import sqrt


def distance(a,b):
  return sqrt((a[0]-b[0])**2 +(a[1]-b[1])**2)


def solution(numbers, hand):

  dic={
    1:[0,0],
    2:[0,1],
    3:[0,2],
    4:[1,0],
    5:[1,1],
    6:[1,2],
    7:[2,0],
    8:[2,1],
    9:[2,2],
    0:[3,1]
  }
  answer = ''
  left_hand_number=[1,4,7]
  right_hand_number=[3,6,9]
  left_hand_spot=[]
  right_hand_spot=[]

  for number in numbers:
    if number in left_hand_number:
      left_hand_spot=dic[number]
      answer+='l'
    elif number in right_hand_number:
      right_hand_spot=dic[number]
      answer+='r'
    else:
      if 


  return answer