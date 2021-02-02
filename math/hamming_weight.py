
def hamming_weight(n):
    """
    No.191 Number of 1 bits

    Given an integer, return the number of 1 bits in its binary representation.

    e.g.
    input: 3 (binary 00000000000000000000000000000011)
    output: 2

    Date: 02/02/2021
    """
    res = 0
    while n:
        res += n & 1
        n >>= 1
    return res


if __name__ == "__main__":
    num = 3
    print(hamming_weight(num)) # res = 2