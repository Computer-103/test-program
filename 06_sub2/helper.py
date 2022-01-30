import random

# - (+) +
num_idx = 0o3000

for i in range(0o1000):
    if i % 2:
        sign = "+"
    else:
        sign = "-"
    print("%04o@ %s%010o" % (num_idx, sign, random.randint(0, 0o7777777777)))
    num_idx += 1

num_idx = 0o3000

l_idx = 0o0000
x_idx = 0o2000

for i in range(32):
    print("%04o@ +00 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, num_idx - 1, num_idx - 1))
    l_idx += 1
    print("%04o@ +10 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx, num_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +20 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +45 %04o %04o" % (l_idx, x_idx, x_idx))
    l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx, num_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +30 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1
    print("%04o@ +40 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    l_idx += 1
    num_idx += 2
    print("%04o@ +45 %04o %04o" % (l_idx, num_idx - 1, num_idx - 1))
    l_idx += 1
    # print("%04o@ +50 %04o %04o" % (l_idx, num_idx, num_idx + 1))
    # l_idx += 1
    # num_idx += 2
    # print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    # l_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, num_idx, num_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +60 %04o %04o" % (l_idx, num_idx, x_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +45 %04o %04o" % (l_idx, x_idx, x_idx))
    l_idx += 1
    # print("%04o@ +05 %04o %04o" % (l_idx, num_idx, num_idx))
    # l_idx += 1
    # num_idx += 1
    # print("%04o@ +70 %04o %04o" % (l_idx, num_idx, x_idx))
    # l_idx += 1
    # num_idx += 1
    # print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    # l_idx += 1


print("%04o@ +54 0000 0000" % l_idx)

print()

