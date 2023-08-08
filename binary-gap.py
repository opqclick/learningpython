# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    _bin = ('{0:08b}'.format(N))
    print(len(_bin))
    pass


solution(int(input("Place your integer number and press enter: " )))