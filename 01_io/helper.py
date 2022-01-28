import random

for x in range(128):
    if (x % 2):
        y = "45"
    else:
        y = "55"
    print("%04o@ +%s %04o %04o" % (x, y, 0o1000 + x, 0o2000 + x))

for x in range(128):
    if (x % 2):
        y = "45"
    else:
        y = "55"
    print("%04o@ +%s %04o %04o" % (128 + x, y, 0o2000 + x, 0o2000 + x))

for x in range(128):
    if (x % 2):
        y = "07"
    else:
        y = "27"
    print("%04o@ +%s %04o %04o" % (256 + x, y, 0o0000, 0o1000 + x))

for x in range(128):
    if (x % 2):
        y = "45"
    else:
        y = "55"
    print("%04o@ +%s %04o %04o" % (384 + x, y, 0o1000 + x, 0o1000 + x))

for x in range(128):
    if (x % 2):
        y = "+"
    else:
        y = "-"
    print("%04o@ %s%010o" % (0o1000 + x, y, random.randint(0, 0o7777777777)))

print("")

for x in range(128):
    if (x % 2):
        y = "+"
    else:
        y = "-"
    print("%s%010o" % (y, random.randint+(0, 0o7777777777)))

