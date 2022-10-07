import random
from decimal import Decimal
import time

start_time = time.time()

file = 'xyz.txt'

r0 = 0.1
x0 = 112917.160
y0 = 91608.705

p = 0


def pvv(x0, y0, r0):
    s_vv = 0
    vv = 0
    x0 = Decimal(str(x0))
    y0 = Decimal(str(y0))
    r0 = Decimal(str(r0))
    with open(file, 'r', encoding='utf-8') as points:
        for xy in points:
            xy = xy.strip('\n').split()
            xy = [Decimal(i) for i in xy]
            try:
                vv = (((x0 - xy[0]) ** 2 + (y0 - xy[1]) ** 2) ** (Decimal('1') / Decimal('2')) - r0) ** 2
            except OverflowError:
                print(xy)
            s_vv += vv

    return s_vv


def step(i):
    h = random.uniform(0.1, 1) * random.uniform(-1, 1)
    t = h - (h / 250) * (i - 1)
    if i == 1:
        t = h
    return t


def gen(x0, y0, r0):
    t = 0.001
    for i in range(250):
        childhood1 = []
        for j in range(15):
            xn0 = x0 + step(i)
            yn0 = y0 + step(i)
            rn = r0 + step(i)
            child1 = [xn0, yn0, rn]
            childhood1.append(child1)

        ee1 = []
        for one in childhood1:
            d = pvv(one[0], one[1], one[2])
            ee1.append(d)

        best = childhood1[ee1.index(min(ee1))]
        x0 = best[0]
        y0 = best[1]
        r0 = best[2]

    for i in range(30):
        childhood2 = []
        for j in range(20):
            xn0 = x0 + random.uniform(-1, 1) * t
            yn0 = y0 + random.uniform(-1, 1) * t
            rn = r0 + random.uniform(-1, 1) * t
            child2 = [xn0, yn0, rn]
            childhood2.append(child2)

        ee2 = []
        for one in childhood2:
            d = pvv(one[0], one[1], one[2])
            ee2.append(d)

        best = childhood2[ee2.index(min(ee2))]
        x0 = best[0]
        y0 = best[1]
        r0 = best[2]

    x0 = round(x0, 3)
    y0 = round(y0, 3)
    r0 = round(r0, 3)
    m = round((pvv(x0, y0, r0) / Decimal('131')) ** (Decimal('1') / Decimal('2')), 3)
    return x0, y0, r0, m


f = gen(x0, y0, r0)
print('X0 =', f[0], 'м')
print('Y0 =', f[1], 'м')
print('R =', f[2], 'м')
print('СКО =', f[3], 'м')
print('Время выполнения программы:', round(time.time() - start_time, 0), 'с')
