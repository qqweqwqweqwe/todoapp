def solution(line):
  maxx=-100000
  maxy=-100000
  minx=100000
  miny=100000
  pointset=[]
  n=len(line)
  for i in range(n-1):
    for j in range(i+1, n):
      a,b,e=line[i][0],line[i][1],line[i][2]
      c,d,f=line[j][0],line[j][1],line[j][2]
      mod=a*d-b*c
      if mod==0:
        break
      xval=(b*f-e*d)/mod
      yval=(e*c-a*f)/mod
      if xval==int(xval) and yval==int(yval):
        xval=int(xval)
        yval=int(yval)
        pointset.append([xval,yval])
    minx=min(minx,xval)
    maxx=max(maxx,xval)
    miny=min(miny,yval)
    maxy=max(maxy,yval)
  print(pointset)
  print(maxx,maxy,minx,miny)
  for i in range(maxy,miny-1,-1):
    star=""
    for j in range(maxx,minx-1,-1):
      if [j,i] in pointset:
        star+="*"
      else:
        star+="."
    print(star)
  answer = []
  return answer
solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])