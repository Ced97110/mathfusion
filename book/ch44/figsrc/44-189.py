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

fig, ax = canvas(70)
box(ax, 3, 4, 58, 62, 'sujet', fill=False, dash=True, lw=1.0)
text(ax, 32, 60, r'$GL_2(\mathbb{R})$', 'sujet', 'l', weight='bold')
box(ax, 7, 42, 14, 8, 'sujet', label='Q'); box(ax, 41, 42, 14, 8, 'sujet', label='T')
box(ax, 24, 24, 14, 8, 'resultat', label='QT')
arrow(ax, (14, 41.5), (26, 32.5), 'varie'); arrow(ax, (48, 41.5), (36, 32.5), 'varie')
text(ax, 32, 37.5, 'produit', 'varie', 's')
box(ax, 7, 8, 14, 8, 'autre', label=r'$Q^{-1}$')
arrow(ax, (11, 41.5), (11, 16.5), 'autre', both=True)
text(ax, 13, 29, 'inverse', 'autre', 's', ha='left')
box(ax, 41, 8, 14, 8, 'fixe', label='I'); text(ax, 48, 20, 'neutre', 'fixe', 's')
box(ax, 64, 42, 21, 10, 'limite', label=r'(1 2 ; 2 4)', size='s')
text(ax, 74.5, 36, r'det = 0', 'limite', 's'); text(ax, 74.5, 31, 'dehors', 'limite', 's', weight='bold')
text(ax, 74.5, 58, r'$GL_2(\mathbb{R})$', 'limite', 's') if False else None
save(fig, '44-189')
