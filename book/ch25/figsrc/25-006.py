import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(52)
P = lambda c, r, a: (c[0] + r * math.cos(math.radians(a)), c[1] + r * math.sin(math.radians(a)))
r = 11
for c, span, nm, d, k, lab in [((16, 30), 90, '1/4 de tour', '90°', 1, '1 angle droit'), ((44, 30), 180, '1/2 tour', '180°', 2, '2 angles droits'), ((72, 30), 360, '1 tour', '360°', 4, '4 angles droits')]:
    n = int(span / 3)
    poly(ax, [c] + [P(c, r, span * i / n) for i in range(n + 1)], 'sujet')
    arc(ax, c, r, 0, 360, 'sujet', 1.0)
    for j in range(k + 1 if span < 360 else k):
        line(ax, [c, P(c, r, 90 * j)], 'encre', lw=0.6)
    for j in range(k):
        a = 90 * j
        line(ax, [P(c, 3.5, a), P(c, 4.95, a + 45), P(c, 3.5, a + 90)], 'encre', lw=0.6)
    text(ax, c[0], 46, nm, 'fixe', 's')
    text(ax, c[0], 11, d, 'sujet', 'l', weight='bold')
    text(ax, c[0], 5, lab, 'fixe', 's')
save(fig, '25-006')
