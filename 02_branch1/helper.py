import random

num_idx = 0o3400
b_idx = 0o3000
d_idx = 0o3001
f_idx = 0o3002
h_idx = 0o3003
x_idx = 0o3004
y_idx = 0o3005

for i in range(0o200):
    if random.randint(0, 1):
        sign = "-"
    else:
        sign = "+"
    print("%04o@ %s%010o" % (num_idx, sign, random.randint(0, 0o7777777777)))
    num_idx += 1

num_idx = 0o3400

p_idx = 0o0000
q_idx = 0o1000

for i in range(64):
    print("%04o@ +05 %04o %04o" % (p_idx, num_idx, b_idx))
    p_idx += 1
    num_idx += 1
    print("%04o@ +24 %04o %04o" % (p_idx, q_idx, d_idx))
    p_idx += 1
    print("%04o@ +64 %04o %04o" % (q_idx, q_idx + 1, x_idx))
    q_idx += 1
    print("%04o@ +45 %04o %04o" % (q_idx, b_idx, b_idx))
    q_idx += 1
    print("%04o@ +45 %04o %04o" % (q_idx, d_idx, d_idx))
    q_idx += 1
    print("%04o@ +15 %04o %04o" % (q_idx, num_idx, f_idx))
    q_idx += 1
    num_idx += 1
    print("%04o@ +64 %04o %04o" % (q_idx, p_idx, h_idx))
    q_idx += 1
    print("%04o@ +64 %04o %04o" % (p_idx, p_idx + 1, y_idx))
    p_idx += 1
    print("%04o@ +55 %04o %04o" % (p_idx, f_idx, f_idx))
    p_idx += 1
    print("%04o@ +55 %04o %04o" % (p_idx, h_idx, h_idx))
    p_idx += 1

print("%04o@ +14 0000 0000" % p_idx)

print()
