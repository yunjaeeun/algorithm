# # def rotate_mag(sequence, mag, rotate):
# #     if rotate == 1:
# #         num = mag.pop()
# #         mag.insert(0, num)
# #     else:
# #         num = mag.pop(0)
# #         mag.append(num)
# #
# #     if sequence == 1:
# #         if mag_1[2] != mag_2[6]:
# #             if rotate == 0:
# #                 rotate_mag(2, mag_2, 1)
# #             else:
# #                 rotate_mag(2, mag_2, -1)
# #
# #     elif sequence == 2:
# #         if mag_1[2] != mag_2[6]:
# #             if rotate == 0:
# #                 rotate_mag(1, mag_1, 1)
# #             else:
# #                 rotate_mag(1, mag_1, -1)
# #
# #         if mag_2[2] != mag_3[6]:
# #             if rotate == 0:
# #                 rotate_mag(3, mag_3, 1)
# #             else:
# #                 rotate_mag(3, mag_3, -1)
# #     elif sequence == 3:
# #         if mag_2[2] != mag_3[6]:
# #             if rotate == 0:
# #                 rotate_mag(2, mag_2, 1)
# #             else:
# #                 rotate_mag(2, mag_2, -1)
# #
# #         if mag_3[2] != mag_4[6]:
# #             if rotate == 0:
# #                 rotate_mag(4, mag_4, 1)
# #             else:
# #                 rotate_mag(4, mag_4, -1)
# #     else:
# #         if mag_3[2] != mag_4[6]:
# #             if rotate == 0:
# #                 rotate_mag(3, mag_3, 1)
# #             else:
# #                 rotate_mag(3, mag_3, -1)
#
#
# # T = int(input())
# #
# # for tc in range(1, 1 + T):
# #     K = int(input())
# #
# #     mag_1 = list(map(int, input().split()))
# #     mag_2 = list(map(int, input().split()))
# #     mag_3 = list(map(int, input().split()))
# #     mag_4 = list(map(int, input().split()))
# #
# #     for _ in range(K):
# #         sequence, rotate = map(int, input().split())
# #
# #         if sequence == 1:
# #             rotate_mag(sequence, mag_1, rotate)
# #         elif sequence == 2:
# #             rotate_mag(sequence, mag_2, rotate)
# #         elif sequence == 3:
# #             rotate_mag(sequence, mag_3, rotate)
# #         else:
# #             rotate_mag(sequence, mag_4, rotate)
# #
# #     print(mag_1)
# #     print(mag_2)
# #     print(mag_3)
# #     print(mag_4)
# #
# #     result = 0
# #     result += mag_1[0] * 1
# #     result += mag_2[0] * 2
# #     result += mag_3[0] * 4
# #     result += mag_4[0] * 8
# #
# #     print(f"#{tc} {result}")
#
#
# def test(sequence, arr, rotate):
#     if sequence in dum:
#         return
#     else:
#         dum.append(sequence)
#         if rotate == 1:
#             num = arr.pop()
#             arr.insert(0, num)
#         else:
#             num = arr.pop(0)
#             arr.append(num)
#
#         # 순서가 1보다 크고 현재
#         if sequence > 0 and magnetic[sequence - 1][2] != magnetic[sequence][6]:
#             test(sequence - 1, magnetic[sequence - 2], -rotate)
#
#         if sequence < 3 and magnetic[sequence][2] != magnetic[sequence - 1][6]:
#             test(sequence + 1, magnetic[sequence], -rotate)
#
#
# T = int(input())
#
# for tc in range(1, 1 + T):
#     K = int(input())
#
#     magnetic = [list(map(int, input().split())) for _ in range(4)]
#
#     for _ in range(K):
#         sequence, rotate = map(int, input().split())
#
#         dum = []
#         test(sequence - 1, magnetic[sequence - 1], rotate)
#
#     result = 0
#     result += magnetic[0][0] * 1
#     result += magnetic[1][0] * 2
#     result += magnetic[2][0] * 4
#     result += magnetic[3][0] * 8
#     print(magnetic)
#
#     print(f"#{tc} {result}")

def test(sequence, arr, rotate):
    if sequence in dum:
        return
    else:
        dum.append(sequence)
        if rotate == 1:
            num = arr.pop()
            arr.insert(0, num)
        else:
            num = arr.pop(0)
            arr.append(num)

        # Check the left and right neighbors
        if sequence > 1 and magnetic[sequence - 2][2] != magnetic[sequence - 1][6]:
            test(sequence - 1, magnetic[sequence - 2], -rotate)

        if sequence < 4 and magnetic[sequence - 1][2] != magnetic[sequence][6]:
            test(sequence + 1, magnetic[sequence], -rotate)


# Read input
T = int(input())

for tc in range(1, T + 1):
    K = int(input())

    magnetic = [list(map(int, input().split())) for _ in range(4)]

    for _ in range(K):
        sequence, rotate = map(int, input().split())
        dum = []  # Initialize dum for each operation
        test(sequence, magnetic[sequence - 1], rotate)

    result = 0
    result += magnetic[0][0] * 1
    result += magnetic[1][0] * 2
    result += magnetic[2][0] * 4
    result += magnetic[3][0] * 8

    print(f"#{tc} {result}")