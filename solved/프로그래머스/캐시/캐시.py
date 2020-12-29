def solution(cacheSize, cities):
    
    answer = 0

    if cacheSize:

        cities = [x.upper() for x in cities]
        cache = ['' for _ in range(cacheSize)]

        cache = []

        ind = 0
        for city in cities:

            if city in cache:
                cache.pop(cache.index(city))
                cache += [city]
                answer += 1
            else:
                if ind < cacheSize:
                    cache.append(city)
                    ind += 1
                else:
                    cache = cache[1:]+[city]
                answer += 5

        return answer
    else:
        return len(cities)*5