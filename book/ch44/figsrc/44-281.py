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

fig, ax = canvas(56)
cs = 10
mat(ax, 4, 6, cs, [['1', '2'], ['3', '4']], [['fixe', 'fixe'], ['sujet', 'sujet']])
mat(ax, 30, 28, cs, [['5', '6'], ['7', '8']], [['autre', 'fixe'], ['autre', 'fixe']])
for i in range(2):
    for j in range(2):
        box(ax, 30 + j * cs, 6 + (1 - i) * cs, cs, cs, 'resultat' if (i, j) == (1, 0) else 'fixe', fill=(i, j) == (1, 0), label='43' if (i, j) == (1, 0) else None, dash=(i, j) != (1, 0))
text(ax, 54, 47, 'terme à terme :', 'fixe', 's', ha='left')
text(ax, 54, 38, r'$3 \times 5 = 15$', 'varie', 'm', ha='left')
text(ax, 54, 30, r'$4 \times 7 = 28$', 'varie', 'm', ha='left')
text(ax, 54, 20, r'$15 + 28 = 43$', 'resultat', 'm', ha='left', weight='bold')
save(fig, '44-281')
