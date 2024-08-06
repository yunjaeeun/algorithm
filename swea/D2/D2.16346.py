T = int(input())


def find_str(key, mix):
    key_length = len(key)
    string_length = len(mix)

    for i in range(string_length - key_length + 1):
        string = mix[i:i + key_length]

        if string == key:
            return 1
    return 0


for tc in range(1, T + 1):
    key_str = input()
    mix_str = input()

    result = find_str(key_str, mix_str)
    print(f"#{tc} {result}")
