def count_bits(n):   
    binary = bin(n)
    count = 0
    for c in binary:
        if c == "1":
            count = count +1
   
    return count   

assert count_bits(0) == 0
assert count_bits(4) == 1
assert count_bits(7) == 3
assert count_bits(9) == 2
assert count_bits(10) == 2