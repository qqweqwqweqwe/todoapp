


def distance(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])

def solution(numbers, hand):
  answer = ''

  left_keys={
    1:[0,0],
    4:[1,0],
    7:[2,0]
  }

  right_keys={
    3:[0,2],
    6:[1,2],
    9:[2,2]
  }

  middle_keys={
    2:[0,1],
    5:[1,1],
    8:[2,1],
    0:[3,1]
  }

  left_spot=[3,0]
  right_spot=[3,2]

  for number in numbers:
    if number in left_keys.keys():
      answer+='L'
      left_spot=left_keys[number]
    elif number in right_keys.keys():
      answer+='R'
      right_spot=right_keys[number]
    else:
      if distance(left_spot,middle_keys[number])==distance(right_spot,middle_keys[number]):
        if hand=='right':
          right_spot=middle_keys[number]
          answer+='R'
        else:
          left_spot=middle_keys[number]
          answer+='L'
      elif distance(left_spot,middle_keys[number])<distance(right_spot,middle_keys[number]):
        answer+='L'
        left_spot=middle_keys[number]
      elif distance(left_spot,middle_keys[number])>distance(right_spot,middle_keys[number]):
        answer+='R'
        right_spot=middle_keys[number]

  return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	,"left"))