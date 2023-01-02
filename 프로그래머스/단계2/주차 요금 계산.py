import math

enterdict={}


def timediff(a,b):
  b=b.split(':')
  a=a.split(':')
  return (int(b[0])-int(a[0])-1)*60+60+int(b[1])-int(a[1])

def solution(fees, records):
  result=[]
  defaulttime=fees[0]
  defaultcost=fees[1]
  perminute=fees[2]
  percost=fees[3]
  for record in records:
    record=record.split(' ')
    if record[1] in enterdict.keys():
      enterdict[record[1]].append(record[0])
    else:
      enterdict[record[1]]=[record[0]]
  for key in sorted(enterdict.keys()):
    if len(enterdict[key])%2:
      enterdict[key].append('23:59')
    print(enterdict[key])
    tm=0
    for i in range(0, len(enterdict[key])-1,2):
      tm+=timediff(enterdict[key][i], enterdict[key][i+1])

    totalcost=defaultcost+math.ceil(max(tm-defaulttime,0)/perminute)*percost
    result.append(totalcost)
  return result


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))