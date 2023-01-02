from queue import Queue
def solution(bridge_length, weight, truck_weights):
  q=Queue()
  for i in range(bridge_length):
    q.put(0)
  time=0
  totalweight=0
  order=0
  numoftruck=0
  while True:
    time+=1
    temp=q.get()
    if temp!=0:
      numoftruck-=1
      totalweight-=temp
    if totalweight+truck_weights[order]<=weight and numoftruck+1<=bridge_length:
      q.put(truck_weights[order])
      numoftruck+=1
      totalweight+=truck_weights[order]
      order+=1
      if order==len(truck_weights):
        return time+bridge_length
    else:
      q.put(0)

print(solution(2, 10, [7, 4, 5, 6]))