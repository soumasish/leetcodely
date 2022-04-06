

def longestMatchingGroup(S):
    tile_list = S.split(',')
    max_count, curr_count = 1, 1
    prev = tile_list[0]
    for i in range(1, len(tile_list)):
        curr = tile_list[i]
        if prev[2] == curr[0]:
            curr_count += 1
        else:
            max_count = max(max_count, curr_count)
            curr_count = 1
        prev = curr
    max_count = max(curr_count, max_count)
    return max_count


print(longestMatchingGroup("6-3"))
print(longestMatchingGroup("1-2,1-2"))
print(longestMatchingGroup("1-1,3-5,5-2,2-3,2-4"))
print(longestMatchingGroup("5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5"))
print(longestMatchingGroup("1-1,3-5,5-5,5-4,4-2,1-3"))
print(longestMatchingGroup("1-2,2-2,3-3,3-4,4-5,1-1,1-2"))


