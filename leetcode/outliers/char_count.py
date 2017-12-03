import collections

def char_count(string):
    count_map = collections.Counter(string)
    return len(count_map)

if __name__ == '__main__':
    print(char_count('abcdeff'))