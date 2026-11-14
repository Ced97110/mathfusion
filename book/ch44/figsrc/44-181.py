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
s = 11
PL = axes2(ax, 22, 30, s, 1.6, 1.6, 1.6, 1.6); PR = axes2(ax, 66, 30, s, 1.6, 1.6, 1.6, 1.6)
text(ax, 22, 56, 'T d’abord, puis Q', 'encre', 'm', weight='bold'); text(ax, 66, 56, 'Q d’abord, puis T', 'encre', 'm', weight='bold')
text(ax, 44, 30, r'$\neq$', 'limite', 'xl', weight='bold')
for P in (PL, PR):
    arc(ax, P, 10, 80)
    disc(ax, *P(1, 0), 1.2, 'sujet'); text(ax, *P(1.05, -0.38), '(1, 0)', 'sujet', 's')
text(ax, 22, 7, 'T garde (1, 0)', 'sujet', 's')
text(ax, *PL(0.85, 0.85), 'Q', 'varie', 'm', weight='bold'); text(ax, *PR(0.85, 0.85), 'Q', 'varie', 'm', weight='bold')
disc(ax, *PL(0, 1), 1.2, 'resultat'); text(ax, *PL(0.55, 1.28), '(0, 1)', 'resultat', 's')
disc(ax, *PR(0, 1), 1.2, 'fixe'); text(ax, *PR(0.55, 1.28), '(0, 1)', 'fixe', 's')
arrow(ax, PR(0, 0.85), PR(0, -0.85), 'varie', curve=-0.5); text(ax, *PR(0.62, -0.5), 'T', 'varie', 'm', weight='bold')
disc(ax, *PR(0, -1), 1.2, 'autre'); text(ax, *PR(0.6, -1.3), '(0, −1)', 'autre', 's')
save(fig, '44-181')
