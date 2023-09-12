def fun(n):
    count = 0
    positions = []
    position = 0
    num = n
    # string = ""
    while(n):           # n = 161
        count += n&1
        if n&1:
            # string += str(len(n) - position)
            positions.insert(0, len(bin(num)[2:]) - position)
            print(bin(num)[2:])
        position += 1
        n >>= 1
    positions.insert(0, count)
    return positions

if __name__ == "__main__":
    # n = 161
    result = fun(161)
    print('\n'.join(map(str, result)))