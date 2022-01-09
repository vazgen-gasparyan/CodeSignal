"""Input/Output

[execution time limit] 4 seconds (py3)
[input] array.integer numbers

  An array of integers.


[output] array.integer

  Return an array, where the i-th element equals 1 if the triple
  (numbers[i], numbers[i+1], numbers[i+2]) is a zigzag, and 0 otherwise.

For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];
Since all the elements of numbers are increasing, there are no zigzags.

For numbers = [10000, 10000, 10000], the output should be solution(numbers) = [0]
Since all the elements of numbers are the same, there are no zigzags."""


def solution(numbers):
    li = []
    for x, y, z in zip(numbers[:-2], numbers[1:-1], numbers[2:]):
        li.append(1) if x<y>z or x>y<z else li.append(0)
    return li

mylist = list(map(int, input().split()))
true = all([True if 1<=i<=(10**9) else False for i in mylist])
while not 3<=len(mylist)<=100 or not true:
    mylist = list(map(int, input().split()))
