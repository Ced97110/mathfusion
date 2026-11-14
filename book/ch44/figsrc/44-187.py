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

fig, ax = canvas(60)
cs = 10
mat(ax, 4, 6, cs, [['0', '−1'], ['1', '0']], [['sujet', 'sujet'], ['fixe', 'fixe']])
mat(ax, 30, 28, cs, [['0', '1'], ['−1', '0']], [['autre', 'fixe'], ['autre', 'fixe']])
for i in range(2):
    for j in range(2):
        on = i == 0
        box(ax, 30 + j * cs, 6 + (1 - i) * cs, cs, cs, 'resultat' if on else 'fixe', fill=on, label=('1', '0')[j] if on else None, dash=not on)
text(ax, 14, 2, r'$Q$', 'sujet', 'm'); text(ax, 56, 46, r'$Q^{-1}$', 'autre', 'm')
text(ax, 54, 22, 'ligne 1 × colonne 1 :', 'fixe', 's', ha='left')
text(ax, 54, 17, r'$0 \times 0 + (-1) \times (-1) = 1$', 'resultat', 's', ha='left')
text(ax, 54, 10, 'ligne 1 × colonne 2 :', 'fixe', 's', ha='left')
text(ax, 54, 5, r'$0 \times 1 + (-1) \times 0 = 0$', 'resultat', 's', ha='left')
save(fig, '44-187')
