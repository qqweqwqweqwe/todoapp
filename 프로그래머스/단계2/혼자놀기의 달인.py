

def solution(cards):
  card_dict={}
  maxnum=0
  for card in cards:
    card_dict[card]=[]
    

  for i in range(len(cards)):
    start=i+1
    next=cards[i]
    cur=i+1
    card_dict[start].append(start)
    while start!=next:
      card_dict[start].append(next)
      cur=next
      next=cards[cur-1]
  
  for i in range(1,len(cards)):
    for j in range(i+1,len(cards)+1):
      if set(card_dict[i]) & set(card_dict[j]):
        continue
      else:
        maxnum=max(maxnum,len(card_dict[i])*len(card_dict[j]))
  return maxnum


solution([8,6,3,7,2,5,1,4])