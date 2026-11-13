import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes2(ax, cx, cy, s, xl, xr, yd, yu):
    arrow(ax, (cx - xl * s, cy), (cx + xr * s, cy), 'fixe', lw=0.7)
    arrow(ax, (cx, cy - yd * s), (cx, cy + yu * s), 'fixe', lw=0.7)
    return lambda x, y: (cx + x * s, cy + y * s)
def arc(ax, P, a0, a1, role='varie'):
    d = math.radians(a1 - a0)
    p = (math.cos(math.radians(a0)), math.sin(math.radians(a0))); q = (math.cos(math.radians(a1)), math.sin(math.radians(a1)))
    arrow(ax, P(*p), P(*q), role, curve=math.tan(d / 4))
def mat(ax, x, y, cs, vals, roles, size='m'):
    for i in range(2):
        for j in range(2):
            box(ax, x + j * cs, y + (1 - i) * cs, cs, cs, roles[i][j], label=vals[i][j], size=size)

fig, ax = canvas(72)
s = 16; P = axes2(ax, 44, 36, s, 1.7, 1.7, 1.7, 1.7)
poly(ax, [P(-1, -1), P(1, -1), P(1, 1), P(-1, 1)], 'fixe', fill=False)
line(ax, [P(-1.3, -1.3), P(1.3, 1.3)], 'sujet', lw=1.8)
arrow(ax, P(0.9, 0.1), P(0.1, 0.9), 'varie', lw=1.2)
disc(ax, *P(1, 0), 1.3, 'sujet'); disc(ax, *P(0, 1), 1.3, 'resultat')
text(ax, *P(1.4, -0.22), '(1, 0)', 'sujet', 'm'); text(ax, *P(0.0, 1.3), '(0, 1)', 'resultat', 'm')
text(ax, *P(1.35, 1.5), r'$y = x$', 'sujet', 'm')
text(ax, 44, 68, r'$QT$ : $(x,\ y)\ \mapsto\ (y,\ x)$', 'varie', 'l')
text(ax, 44, 4, r'$QT = rs$ du carré', 'encre', 'm')
save(fig, '44-180')
