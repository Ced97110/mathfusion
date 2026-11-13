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

fig, ax = canvas(64)
xs = [13, 44, 75]; y = 28
text(ax, 38, 56, r'$A$', 'varie', 14, weight='bold'); text(ax, 50, 56, r'$B$', 'varie', 14, weight='bold')
arrow(ax, (50, 50), (38, 50), 'varie', lw=1.4, curve=-0.5)
text(ax, 44, 43, 'on lit de droite à gauche', 'encre', 's')
for x, (lab, r) in zip(xs, [(r'$(x,\ y)$', 'sujet'), (r'$(x,\ -y)$', 'fixe'), (r'$(y,\ x)$', 'resultat')]):
    box(ax, x - 10, y - 5, 20, 10, r, label=lab)
for a, b, lab, sub in [(xs[0], xs[1], '1 : B', r'$T$ réflexion'), (xs[1], xs[2], '2 : A', r'$Q$ quart de tour')]:
    arrow(ax, (a + 10.5, y), (b - 10.5, y), 'varie'); text(ax, (a + b) / 2, y + 4, lab, 'varie', 'm', weight='bold')
    text(ax, (a + b) / 2, y - 8.5, sub, 'encre', 's')
brace(ax, xs[0] - 10, xs[2] + 10, 13, 'autre', label='AB : B d’abord, puis A')
save(fig, '44-179')
