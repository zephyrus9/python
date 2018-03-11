def search(sequence, number, lower=0, upper=None):

    if upper == None:
        upper = len(sequence)
    if upper == lower:
        assert number == sequence[upper]
        return upper
    else:
        middle = (upper + lower) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle, upper)
        else:
            return search(sequence, number, lower, middle - 1)

if __name__ == '__main__':
    seq = list(range(1:100:2))
    search(seq, 34)

