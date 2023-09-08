def recursive_b_s(list, target):
    if len(list) == 0:
        return False
    else:
      midpoint = len(list)//2

      if list[midpoint] == target:
        return True
      elif list[midpoint] < target:
        return recursive_b_s(list[midpoint + 1 : ], target)
      else:
          return recursive_b_s(list[: midpoint], target)

def verify(result):

     print(' target found : ' , result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = recursive_b_s(numbers, 3)

verify(result)
