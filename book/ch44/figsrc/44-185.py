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
s = 7
PL = axes2(ax, 24, 10, s, 1.8, 1.8, 0.8, 6.2); PR = axes2(ax, 54, 10, s, 1.0, 4.4, 0.8, 6.2)
text(ax, 24, 67, r'det $A$ = 1 $\neq$ 0', 'resultat', 'm', weight='bold'); text(ax, 24, 62, 'inversible', 'resultat', 'm')
text(ax, 66, 67, r'det $A$ = 4 − 4 = 0', 'limite', 'm', weight='bold'); text(ax, 66, 62, 'pas inversible', 'limite', 'm')
poly(ax, [PL(0, 0), PL(1, 0), PL(1, 1), PL(0, 1)], 'sujet')
poly(ax, [PL(0, 0), PL(0, 1), PL(-1, 1), PL(-1, 0)], 'resultat')
text(ax, *PL(0.5, 1.7), 'carré', 'sujet', 's'); text(ax, *PL(-1.0, 2.0), 'image', 'resultat', 's')
poly(ax, [PR(0, 0), PR(1, 0), PR(1, 1), PR(0, 1)], 'sujet')
line(ax, [PR(0, 0), PR(3, 6)], 'limite', lw=2.2)
text(ax, *PR(2.3, 1.6), 'carré', 'sujet', 's'); text(ax, *PR(3.3, 4.9), 'image', 'limite', 's', ha='left'); text(ax, *PR(3.3, 4.2), 'droite', 'limite', 's', ha='left')
save(fig, '44-185')
