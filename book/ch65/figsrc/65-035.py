import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

vals = [1, 2, 3]
fig, ax = canvas(66)
f = numberline(ax, 12, 72, 24, 0, 4, 1, labels=False, arrow_right=False)
text(ax, 44, 62, '1. on numérote les racines', 'sujet', 's')
for k, v in enumerate(vals):
    disc(ax, f(v), 24, 3.2, 'sujet', label=r'$r_%d$' % (k + 1), size='s')
    text(ax, f(v), 17, '= %d' % v, 'sujet', 's')
text(ax, 44, 56, '2. une différence par paire', 'varie', 's')
prod = 1
for (a, b) in [(1, 2), (1, 3), (2, 3)]:
    d = vals[a - 1] - vals[b - 1]
    prod *= d
    xa, xb = f(vals[a - 1]), f(vals[b - 1])
    far = (a, b) == (1, 3)
    arrow(ax, (xa + 1.5, 28), (xb - 1.5, 28), 'varie', lw=0.9, curve=-0.5 if far else -0.9)
    ym = 28 + abs(xb - xa) * (0.25 if far else 0.45) + 2.8
    if far:
        ym += 4.0
    text(ax, (xa + xb) / 2, ym, '%d' % d if d >= 0 else '−%d' % -d, 'varie', 'm', weight='bold')
assert prod == -2
text(ax, 44, 9, '3. on multiplie', 'resultat', 's')
text(ax, 44, 3.5, r'$D=(-1)\times(-2)\times(-1)=-2$', 'resultat', 'm', weight='bold')
save(fig, '65-035')
