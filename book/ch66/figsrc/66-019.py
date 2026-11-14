import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(60)
cy, r = 28, 14
for cx, n in [(22, 2), (66, 4)]:
    disc(ax, cx, cy, r, 'fixe', fill=False)
    line(ax, [(cx - r - 3, cy), (cx + r + 3, cy)], 'fixe')
    for k in range(n):
        a = 360 * k / n; p = P(cx, cy, r, a); disc(ax, p[0], p[1], 1.6, 'sujet')
    text(ax, cx + r + 3.5, cy + 3, '1', 'sujet')
    text(ax, cx - r - 4.5, cy + 3, '−1', 'sujet')
    text(ax, cx, 52, r'$z^{%d}=1$ : %d racines' % (n, n), 'sujet', 'm')
text(ax, 66, cy + r + 4, 'complexe', 'varie', 's'); text(ax, 66, cy - r - 4, 'complexe', 'varie', 's')
save(fig, '66-019')
