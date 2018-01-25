def sort_by_last_letter(arr):
    def last_letter(s):
        return s[-1]
    return sorted(arr, key=last_letter)


def sort_by_last_letter_lambda(arr):
    return sorted(arr, key=lambda s: s[-1])


if __name__ == '__main__':
    print(sort_by_last_letter_lambda(['penguin', 'octopus', 'rhino']))
