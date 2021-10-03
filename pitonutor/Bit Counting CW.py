

def count_bits(n):
    bit_n = 0
    while n >= 1:
        n_ostatok = n % 2
        n = n // 2
        if n_ostatok == 1:
            bit_n += 1
    return bit_n

print(count_bits(7))