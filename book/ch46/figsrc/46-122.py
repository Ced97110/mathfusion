import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
items = [(0, 'ℤ0', 1, [0]), (6, 'x', 2, [0, 6]), (4, 'x', 3, [0, 4, 8]), (3, 'x', 4, [0, 3, 6, 9]), (2, 'x', 6, [0, 2, 4, 6, 8, 10]), (1, 'x', 12, list(range(12)))]
for i, (g, _, n, mem) in enumerate(items):
    cx = 15 + (i % 3) * 29; cy = 52 - (i // 3) * 33; R = 9
    for k in range(12):
        x = cx + R * math.sin(math.radians(30 * k)); y = cy + R * math.cos(math.radians(30 * k))
        if k in mem: disc(ax, x, y, 1.7, 'sujet')
        else: disc(ax, x, y, 0.7, 'fixe')
    text(ax, cx, cy - 14.5, rf'$\langle {g}\rangle$ : {n} élément' + ('s' if n > 1 else ''), 'sujet', 's')
text(ax, 44, 69, 'un sous-groupe par diviseur de 12', 'encre', 'm')
save(fig, '46-122')
