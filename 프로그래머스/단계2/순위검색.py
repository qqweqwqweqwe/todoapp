infodict={}

for lang in ['cpp','java','python','-']:
  for end in ['backend','frontend','-']:
    for career in ['junior','senior','-']:
      for food in ['chicken','pizza','-']:
        infodict[lang+end+career+food]=[]

def solution(infos, querys):
  answer=[]
  for info in infos:
    info=info.split()
    for lang in [info[0],'-']:
      for end in [info[1],'-']:
        for car in [info[2],'-']:
          for food in [info[3],'-']:
            infodict[lang+end+car+food].append(int(info[4]))
  
  for i in infodict.values():
    i.sort()

  for query in querys:
    query=query.replace(' and ','').split(' ')
    infos=query[0]
    point=int(query[1])
    infolist=infodict[infos]
    start,end=0,len(infolist)-1
    mid=0
    while end > start:
      mid=(start+end)//2
      if infolist[mid]>=point:
        end=mid
      else:
        start=mid+1
    answer.append(len(infolist)-1-mid)
  

  
  return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	,["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	))