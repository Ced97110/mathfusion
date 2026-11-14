import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(59)
def arcp(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]

cx, cy, r = 44, 28, 21
a0, a1 = 90 - 57.3, 90 + 57.3
P = (cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1)))
Q = (cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)))
poly(ax, [(cx, cy)] + arcp(cx, cy, r, a0, a1), 'fixe')
line(ax, arcp(cx, cy, r, a0, a1), 'varie', lw=2.0)
line(ax, [(cx, cy), P], 'sujet', lw=1.3)
line(ax, [(cx, cy), Q], 'sujet', lw=1.3)
text(ax, P[0] - 3.5, P[1] + 1, r'$P$', 'encre', 'm')
text(ax, Q[0] + 3.5, Q[1] + 1, r'$Q$', 'encre', 'm')
text(ax, cx, cy - 4.5, r'$O$', 'encre', 'm')
text(ax, cx, cy + 7, 'angle 2', 'fixe', 's')
text(ax, cx, 55, "l'arc contient 2 fois r", 'varie', 's')
box(ax, 23, 8.5, 21, 7, 'varie', label='r = 3', size='s')
box(ax, 44, 8.5, 21, 7, 'varie', label='r = 3', size='s')
brace(ax, 23, 65, 8.5, 'varie', label='arc s = 3 × 2 = 6 cm')
save(fig, '29-092')
