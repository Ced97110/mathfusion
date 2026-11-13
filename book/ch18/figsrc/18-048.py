import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(56)
u = 4
x0, y0 = 6, 10
for i in range(5):
    for j in range(5):
        r = 'autre' if (i >= 2 and j >= 2) else 'sujet'
        box(ax, x0 + i * u, y0 + j * u, u, u, r, r=0.1, lw=0.5)
text(ax, x0 + 2.5 * u, y0 - 4, r'$a=5$', 'sujet', 's'); text(ax, x0 + 3.5 * u, y0 + 5 * u + 4, r'$b=3$', 'autre', 's')
text(ax, 38, 42, r'$a^2=25$ : tout le carré', 'sujet', 's', ha='left')
text(ax, 38, 31, r'$b^2=9$ : le petit carré', 'autre', 's', ha='left')
arrow(ax, (37, 31), (x0 + 5 * u + 1, 31), 'autre')
text(ax, 38, 18, r'reste $16$', 'resultat', 'm', ha='left')
arrow(ax, (37, 18), (x0 + 3 * u, 18), 'resultat')
save(fig, '18-048')
