def valid(num):
  if num<6 and num>-6:
    return True
  else:
    return False


def solution(dirs):
  route=set()
  x,y=0,0
  for dir in dirs:
    if dir=='U':
      if valid(y+1):
        route.add((x,y,x,y+1))
        route.add((x,y+1,x,y))
        y+=1
    elif dir=='D':
      if valid(y-1):
        route.add((x,y,x,y-1))
        route.add((x,y-1,x,y))
        y-=1
    elif dir=='R':
      if valid(x+1):
        route.add((x,y,x+1,y))
        route.add((x+1,y,x,y))
        x+=1
    elif dir=='L':
      if valid(x-1):
        route.add((x,y,x-1,y))
        route.add((x-1,y,x,y))
        x-=1
  return (len(route))/2


solution("LULLLLLLU")




      



  
