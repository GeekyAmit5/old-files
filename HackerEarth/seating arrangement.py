# incomplete

def facingSeat(n):
    return n//12*12+13-n


def seatType(n):
    if n % 6 == 0 or n % 6 == 1:
        return "WS"
    elif n % 3 == 0 or n % 3 == 1:
        return 'AS'
    return 'MS'


t = int(input())
seats = list(map(int, input().split()))
for seat in seats:
    i = facingSeat(seat)
    print(i, seatType(i))
