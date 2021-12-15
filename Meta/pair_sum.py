import math
from collections import Counter
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
   # Write your code here
    hash_ = Counter(arr)
    done = []
    res = 0
    for key in hash_:

      if key not in done:
        if k - key in hash_:
          if k-key != key:
            res += hash_[key]*hash_[k-key]
            done.append(key)
            done.append(k-key)
          else:
            if hash_[key] > 2:
              res += hash_[key]
              
            else:
              res += 1
            done.append(key)
    return res
      
        

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
