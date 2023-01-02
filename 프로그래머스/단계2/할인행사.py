


def solution(want, number, discount):
  totalnum=0
  want_dict={}
  for i in range(len(want)):
    want_dict[want[i]]=number[i]
    totalnum+=number[i]
  result=0

  for i in range(len(discount)-totalnum+1):
    comp_dict={}
    flag=True
    for d in discount[i:i+totalnum]:
      if d in comp_dict.keys():
        comp_dict[d]+=1
      else:
        comp_dict[d]=1
    
    for w in want:
      try:
        if want_dict[w]!=comp_dict[w]:
          flag=False
          break
      except:
        flag=False
        break
    if flag:
      result+=1
  return result



solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]	)