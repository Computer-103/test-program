import random

for x in range(128):
    if (x % 2):
        y = "07"
    else:
        y = "27"
    print("%04o@ +%s %04o %04o" % (x, y, 0o0000, 0o2000 + x))

for x in range(128):
    if (x % 2):
        y = "45"
    else:
        y = "55"
    print("%04o@ +%s %04o %04o" % (128 + x, y, 0o2000 + x, 0o2000 + x))

print("0400@ +04 0000 0000")

print("")

for x in range(128):
    if (x % 2):
        y = "+"
    else:
        y = "-"
    print("%s%07d" % (y, random.randint(0, 9999999)))

