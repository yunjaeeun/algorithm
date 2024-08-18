T = int(input())

for tc in range(1, T + 1):
    bit = list(input())
    bit_len = len(bit)
    change_bit = ["0"] * bit_len

    result = 0
    while bit != change_bit:
        for i in range(bit_len):
            if bit[i] != change_bit[i]:
                result += 1
                for j in range(i, bit_len):
                    if bit[i] == "1":
                        change_bit[j] = "1"
                    else:
                        change_bit[j] = "0"

    print(f"#{tc} {result}")


