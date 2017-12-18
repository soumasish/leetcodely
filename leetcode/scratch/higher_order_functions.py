def sort_by_last_letter(arr):
    def last_letter(s):
        return s[-1]
    return sorted(arr, key=last_letter)


g = 'global'
def outer(p='param'):
    l ='local'
    def inner():
        print(g, p, l)
    inner()
outer()
