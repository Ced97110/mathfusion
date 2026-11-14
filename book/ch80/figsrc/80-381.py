import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
root = (44, 72)
lv = [[24, 64], [14, 34, 54, 74], [9 + 10 * i for i in range(8)]]
ys = [58, 42, 26]
prev = [root[0]]
def cut(p, q, r):
    d = math.hypot(q[0] - p[0], q[1] - p[1]); ux, uy = (q[0] - p[0]) / d, (q[1] - p[1]) / d
    return [(p[0] + ux * r, p[1] + uy * r), (q[0] - ux * r, q[1] - uy * r)]
for L, (xs, y) in enumerate(zip(lv, ys)):
    py = ys[L - 1] if L > 0 else root[1]
    for i, x in enumerate(xs):
        px = prev[i // 2] if L > 0 else root[0]
        line(ax, cut((px, py), (x, y), 3.4), 'fixe')
    prev = xs
disc(ax, root[0], root[1], 2, 'fixe')
for L, (xs, y) in enumerate(zip(lv, ys)):
    for i, x in enumerate(xs): disc(ax, x, y, 3.2, 'sujet' if i % 2 == 0 else 'varie')
    text(ax, 2.0, y, 'ABC'[L], 'encre', 's', ha='left')
disc(ax, 6, 8, 3, 'sujet'); text(ax, 11, 8, 'bleu', 'sujet', 's', ha='left')
disc(ax, 30, 8, 3, 'varie'); text(ax, 35, 8, 'rouge', 'varie', 's', ha='left')
text(ax, 68, 8, r'$2\times2\times2=8$', 'resultat', 'm')
save(fig, '80-381')
