import heapq

def solution(scoville, K):
  heapq.heapify(scoville)
  count=0
  while scoville[0]<K and len(scoville)>=2:
    first=heapq.heappop(scoville)
    second=heapq.heappop(scoville)
    heapq.heappush(scoville,first+second*2)
    count+=1

  if scoville[0]<K:
    return -1

  return count



#우선순위 힙 

print(solution([1, 2, 3, 9, 10, 12]	,7))