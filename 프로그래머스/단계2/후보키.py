def check(relations,numbers,candlist):
  relationset=set()
  for relation in relations:
    candidate=""
    for i in range(4):
      if numbers[i]=='1':
        candidate+=relation[i]
    relationset.add(candidate)
  if len(relationset)==len(relations):
    candlist.append(numbers)
  
def solution(relations):
  answerlist=[]
  checklist=[]
  for a in ['1','0']: 
    for b in ['1','0']: 
      for c in ['1','0']: 
        for d in ['1','0']:
          checklist.append(a+b+c+d)
  checklist.sort(key=lambda x : x.count('1'))
  for ch in checklist:
    check(relations,ch,answerlist)
  setlist=[]
  for answer in answerlist:
    sl=[]
    for i in range(4):
      if answer[i]=='1':
        sl.append(i)
    setlist.append(sl)
  
  answerlist=setlist      

  answer=answerlist.copy()
  for i in answerlist:
    if i not in answer:
      continue
    for j in answerlist:
      if i==j:
        continue
      else:
        if len(set(i)-set(j))==0:
          if j in answer:
            answer.remove(j)
  print(answer)
  return len(answer)
       
  # 4개면 맞는거임
  


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	)

