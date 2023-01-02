from collections import deque


def solution(cacheSize, cities:list):
    cache = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize:
            if city not in cache:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
                time += 5
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else:
            time += 5
    return time


solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	)