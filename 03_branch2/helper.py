import random

pos_idx = 0o3000
neg_idx = 0o3200
num_idx = 0o3400

for i in range(0o200):
    sign = "+"
    print("%04o@ %s%010o" % (pos_idx, sign, random.randint(0, 0o7777777777)))
    pos_idx += 1

for i in range(0o200):
    sign = "-"
    print("%04o@ %s%010o" % (neg_idx, sign, random.randint(0, 0o7777777777)))
    neg_idx += 1

for i in range(0o400):
    if random.randint(0, 1):
        sign = "-"
    else:
        sign = "+"
    print("%04o@ %s%010o" % (num_idx, sign, random.randint(0, 0o7777777777)))
    num_idx += 1

pos_idx = 0o3000
neg_idx = 0o3200
num_idx = 0o3400

l_idx = 0o0000
m_idx = 0o1000
r_idx = 0o2000
x_idx = 0o2776
stop_idx = 0o2777


for i in range(32):
    print("%04o@ +45 %04o %04o" % (l_idx, num_idx, num_idx))
    l_idx += 1
    num_idx += 1
    print("%04o@ +05 %04o %04o" % (l_idx, pos_idx, pos_idx))
    l_idx += 1
    pos_idx += 1
    print("%04o@ +34 %04o %04o" % (l_idx, stop_idx, m_idx))
    l_idx += 1
    print("%04o@ +55 %04o %04o" % (m_idx, num_idx, num_idx))
    m_idx += 1
    num_idx += 1
    print("%04o@ +15 %04o %04o" % (m_idx, neg_idx, neg_idx))
    m_idx += 1
    neg_idx += 1
    print("%04o@ +34 %04o %04o" % (m_idx, r_idx, stop_idx))
    m_idx += 1
    print("%04o@ +45 %04o %04o" % (r_idx, num_idx, num_idx))
    r_idx += 1
    num_idx += 1
    print("%04o@ +05 %04o %04o" % (r_idx, num_idx, num_idx))
    r_idx += 1
    num_idx += 1
    print("%04o@ +74 %04o %04o" % (r_idx, stop_idx, l_idx))
    r_idx += 1
    print("%04o@ +64 %04o %04o" % (l_idx, l_idx + 1, x_idx))
    l_idx += 1


print("%04o@ +04 0000 0000" % stop_idx)
print("%04o@ +44 0000 0000" % l_idx)

print()
