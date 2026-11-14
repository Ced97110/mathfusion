import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, r, a): return (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
fig, ax = canvas(54)
cy, r = 31, 12
for cx, n, name, a0 in [(15, 3, 'triangle', 90), (44, 4, 'carré', 45), (73, 6, 'hexagone', 90)]:
    disc(ax, cx, cy, r, 'fixe', fill=False)
    pts = [P(cx, cy, r, a0 + 360 * i / n) for i in range(n)]
    poly(ax, pts, 'sujet')
    for p in pts: disc(ax, p[0], p[1], 1.3, 'varie')
    text(ax, cx, cy + r + 4, r'$n=%d$' % n, 'varie', 'm')
    text(ax, cx, cy - r - 4, name, 'sujet', 'm')
brace(ax, 2, 86, 9, 'sujet', label=r'tous : $n$-gone, $n\geq 3$')
save(fig, '66-001')
