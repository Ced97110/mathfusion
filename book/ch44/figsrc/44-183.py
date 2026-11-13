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

fig, ax = canvas(62)
xs = [12, 44, 76]
for y, (l1, c1, l2, c2, res) in [(46, (r'$A^{-1}$', 'autre', 'A', 'varie', r'$AA^{-1} = I$ : retour en P')), (20, ('A', 'varie', r'$A^{-1}$', 'autre', r'$A^{-1}A = I$ : retour en P'))]:
    for x, r, lab in zip(xs, ['sujet', 'fixe', 'sujet'], ['P', "P'", 'P']):
        disc(ax, x, y, 2.5, r); text(ax, x, y + 6, lab, r, 'm', weight='bold')
    for a, b, lab, c in [(xs[0], xs[1], l1, c1), (xs[1], xs[2], l2, c2)]:
        arrow(ax, (a + 3.5, y), (b - 3.5, y), c, lw=1.2); text(ax, (a + b) / 2, y + 4.5, lab, c, 'm', weight='bold')
    text(ax, 44, y - 9, res, 'resultat', 'm')
save(fig, '44-183')
