import random

num_idx = 0o3000

for i in range(0o400):
    if random.randint(0, 1):
        sign = "-"
    else:
        sign = "+"
    x = random.randint(0, 0o7777777777)
    y = random.randint(0, x)
    print("%04o@ %s%010o" % (num_idx, sign, x))
    num_idx += 1
    print("%04o@ %s%010o" % (num_idx, sign, y))
    num_idx += 1

num_idx = 0o3000

l_idx = 0o0000
x_idx = 0o2000

for i in range(32):
    print("%04o@ +02 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, num_idx - 1, num_idx - 1))
    l_idx += 1
    print("%04o@ +12 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx + 1, num_idx + 1))
    l_idx += 1
    print("%04o@ +22 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, x_idx, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx + 1, num_idx + 1))
    l_idx += 1
    print("%04o@ +32 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 2
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1
    print("%04o@ +42 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, num_idx - 1, num_idx - 1))
    l_idx += 1
    print("%04o@ +52 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx + 1, num_idx + 1))
    l_idx += 1
    print("%04o@ +62 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, x_idx, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx + 1, num_idx + 1))
    l_idx += 1
    print("%04o@ +72 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 2
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1

print("2010@ +5555555555")
print("2011@ +6666666666")
print("%04o@ +02 2010 2011" % l_idx)
l_idx += 1
print("%04o@ +45 2011 2011" % l_idx)
l_idx += 1

print("%04o@ +17 0000 0000" % l_idx)

print()
