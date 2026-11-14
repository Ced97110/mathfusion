import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def pol(cx, cy, r, deg): return (cx + r * math.cos(math.radians(deg)), cy + r * math.sin(math.radians(deg)))
def pg(cx, cy, R, n, rot=90): return [pol(cx, cy, R, rot + 360 * k / n) for k in range(n)]
fig, ax = canvas(80)
text(ax, 22, 75, 'dans un groupe', 'sujet', 's'); text(ax, 66, 75, 'avec des nombres', 'autre', 's')
L = (r'$ax = b$', r'$a^{-1}ax = a^{-1}b$', r'$x = a^{-1}b$')
Rr = (r'$5x = 20$', r'$\frac{1}{5}\cdot 5x = \frac{1}{5}\cdot 20$', r'$x = 4$')
ys = (62, 38, 12)
for i in range(3):
    box(ax, 2, ys[i], 40, 10, 'resultat' if i == 2 else 'sujet', label=L[i], size='s')
    box(ax, 46, ys[i], 40, 10, 'resultat' if i == 2 else 'autre', label=Rr[i], size='s')
for i, (a, b) in enumerate(((r'$a^{-1}$ à gauche', r'÷ 5 des deux côtés'), (r'$a^{-1}a = 1$', r'$\frac{1}{5}\cdot 5 = 1$'))):
    for cx, t, r in ((22, a, 'varie'), (66, b, 'varie')):
        arrow(ax, (cx - 6, ys[i] - 0.5), (cx - 6, ys[i + 1] + 10.5), r)
        text(ax, cx - 3.5, (ys[i] + ys[i + 1] + 10) / 2, t, r, 's', ha='left')
save(fig, '44-237')
