import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(cx, cy, r, a0, a1, n=48):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(64)
cx, cy, R = 26, 30, 22
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx - R, cy), (cx + R + 2, cy)], 'fixe')
c30, s30 = math.cos(math.radians(30)), math.sin(math.radians(30))
P = (cx + R * c30, cy + R * s30)
F = (P[0], cy)
line(ax, [(cx, cy), P], 'sujet', lw=1.2)
line(ax, arc(cx, cy, 9, 0, 30), 'varie', lw=1.2)
line(ax, [P, F], 'resultat', lw=1.6)
disc(ax, P[0], P[1], 1.6, 'sujet')
text(ax, cx + 14, cy + 4.5, '30°', 'varie', 'm')
text(ax, F[0] + 6.5, (P[1] + cy) / 2, '0,5', 'resultat', 'm')
text(ax, cx, 58, r'$t=1$ : $30\times 1=30°$', 'varie', 'm')
box(ax, 56, 34, 30, 9, 'fixe', label=r'$2+2\times 0{,}5$')
box(ax, 56, 16, 30, 9, 'resultat', label=r'$h=3$ m')
arrow(ax, (71, 33.5), (71, 25.5), 'varie')
save(fig, '32-009')
