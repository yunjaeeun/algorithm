import random

member = ["재민 D4", "성욱 D4", "민철 D4", "희준 P4", "재은 P4", "희원 S4", "동해 G4", "건준 E2", "학선 G4", "승권 G4"]

blue = []
purple = []

while member:
    player = member.pop(0)
    team_num = random.randrange(1, 11)
    print(team_num)

    if team_num % 2 != 0:
        blue.append(player)
        purple.append(member.pop(0))
    else:
        purple.append(player)
        blue.append(member.pop(0))

    print(blue)
    print(purple)

print("blue_member =", *blue)
print("purple_member =", *purple)
