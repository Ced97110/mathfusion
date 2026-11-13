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

fig, ax = canvas(52)
items = [('G', 'général', 'sujet'), ('L', 'linéaire', 'sujet'), ('2', 'taille 2 × 2', 'varie'), (r'$\mathbb{R}$', 'nombres réels', 'autre')]
w = 17; g = 3.5; x0 = (88 - (4 * w + 3 * g)) / 2
for k, (sym, lab, r) in enumerate(items):
    x = x0 + k * (w + g)
    box(ax, x, 26, w, 17, r, label=sym, size='xl', weight='bold')
    line(ax, [(x + w / 2, 26), (x + w / 2, 21)], r)
    text(ax, x + w / 2, 17.5, lab, r, 's')
text(ax, 44, 7, r'matrices 2 × 2, det $\neq$ 0', 'resultat', 'm')
text(ax, 44, 48, 'chaque lettre porte un sens', 'encre', 'm') if False else None
save(fig, '44-190')
