import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(84)
text(ax, 44, 80, r'$f : n \mapsto -n$', 'varie', 'l')
text(ax, 44, 72, r'départ = arrivée = $\mathbb{Z}$', 'sujet', 's')
f = numberline(ax, 12, 76, 44, -3, 3, 1, arrow_right=False, size='m')
for v in range(-3, 4):
    disc(ax, f(v), 44, 1.4, 'sujet' if v else 'fixe')
for v in (1, 2, 3):
    arrow(ax, (f(-v), 48), (f(v), 48), 'varie', lw=1.0, curve=-0.45 if v > 1 else -0.6, both=True)
box(ax, 2, 14, 40, 11, 'sujet', r'$f(2+3)=-5$', 's')
box(ax, 46, 14, 40, 11, 'autre', r'$f(2)+f(3)=-5$', 's')
text(ax, 44, 19.5, '=', 'resultat', 'xl', weight='bold')
text(ax, 44, 5, 'l’addition est respectée', 'resultat', 's')
save(fig, '48-045')
