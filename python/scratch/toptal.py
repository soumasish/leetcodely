import heapq

def solution(A):
    count, total, target = 0, 0, 0
    heap = []
    for a in A:
        total += a
        heapq.heappush(heap, -1*a)
    target = total/2
    while True:
        item = heapq.heappop(heap)
        count += 1
        total += item
        item = item/2
        total -= item
        heapq.heappush(heap, item)
        if total <= target:
            break
    return count

def solution2(P, S):
    total_people = sum(P)
    count, curr = 0, 0
    heap = []
    for s in S:
        heapq.heappush(heap, -1*s)
    while True:
        item = heapq.heappop(heap)
        curr -= item
        count += 1
        if curr >= total_people:
            break
    return count


def solution3(message, K):
    items = message.split(" ")
    result = ''
    curr_length = 0
    index = 0
    while index < len(items):
        if curr_length + len(items[index]) <= K:
            result += items[index]
            curr_length += len(items[index])
            if index + 1 < len(items):
                if curr_length + 1 + len(items[index + 1]) <= K:
                    result += ' '
                    curr_length += 1
                elif curr_length + 1 + len(items[index + 1]) > K:
                    break
            index += 1
        else:
            break
    return result

print(solution3('a', 21))








