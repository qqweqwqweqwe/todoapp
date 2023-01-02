def tiemdiff(a,b):
  a=a.split(":")
  b=b.split(":")
  if int(a[1])>int(b[1]):
    return (int(a[0])-int(b[0]))*60+int(a[1])-int(b[1])
  else:
    return (int(a[0])-int(b[0])-1)*60+int(a[1])-int(b[1])+60
def solution(m, musicinfos):
  m=m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
  checklist=[]
  for musicinfo in musicinfos:
    musicinfo=musicinfo.split(",")
    musicinfo[3]=musicinfo[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    songtime=tiemdiff(musicinfo[1],musicinfo[0])
    part=""
    for i in range(songtime):
      part+=musicinfo[3][i%len(musicinfo[3])]
    checklist.append([songtime,musicinfo[2],part])
  
  checklenth=0
  checkname=""
  for check in checklist:
    if m in check[2]:
      if check[0]>checklenth:
        checkname=check[1]
        checklenth=check[0]
  if checklenth==0:
    return  "(None)"
  return checkname
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))