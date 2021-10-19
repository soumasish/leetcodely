import heapq


def countMaximumTeams(skill, teamSize, maxDiff):
    min_heap = []
    for item in skill:
        heapq.heappush(item, min_heap)

    teams = 0
    while len(min_heap) >= teamSize:
        store = []
        for _ in range(teamSize):
            if len(store) == 0 or abs(store[-1] - min_heap[0]) <= maxDiff:
                ele = heapq.heappop(min_heap)
                store.append()
        if len(store) == teamSize:
            teams += 1
    return teams



from itertools import combinations
from collections import Counter


def findPasswordStrength(password):
    length = len(password) + 1
    all_substrings = [password[x:y] for x, y in combinations(range(length), r=2)]
    strength = 0
    for item in all_substrings:
        mapper = {}
        for i in item:
            if i not in mapper:
                mapper[i] = 1
        count = 0
        for v in mapper.values():
            count += v
        strength += count
    return strength




