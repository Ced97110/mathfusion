import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
vals = [2, 1, 2, 3, 6, 9]
base, k, w = 16, 3.0, 8
text(ax, 44, 52, r'$N(n,2)$ pour $n=1$ à 6', 'encre', 'm')
line(ax, [(6, base), (84, base)], 'fixe')
for i, v in enumerate(vals):
    cx = 14 + 12.5 * i
    poly(ax, [(cx - w / 2, base), (cx + w / 2, base), (cx + w / 2, base + v * k), (cx - w / 2, base + v * k)], 'sujet')
    text(ax, cx, base + v * k + 3.2, str(v), 'sujet', 'l')
    text(ax, cx, base - 4, str(i + 1), 'encre', 'm')
text(ax, 44, 4, 'degré n', 'fixe', 's')
save(fig, '67-197')
