from collections import deque


def solution(cacheSize, cities):
    answer = 0
    q = deque()
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        city = city.lower()
        if city not in q:
            if len(q) < cacheSize:
                q.append(city)
            else:
                q.popleft()
                q.append(city)
            answer += 5
        elif city in q:
            q.remove(city)
            q.append(city)
            answer += 1
    print(q)
    return answer

cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(2,cities))