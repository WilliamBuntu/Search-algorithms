def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None

def verify(index):
    if index is not None:
        print(f'the target found at {index} position')
    else:
        print('no target found ')


numbers = [1, 2, 3, 4, 5, 0, 7, 8, 9, 10]

result = linear_search(numbers, 9)

verify(result)
