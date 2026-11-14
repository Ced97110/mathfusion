import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_b, _d = box, disc
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _b(ax, x, y, w, h, role, label=label, size=size, **k)
def disc(ax, x, y, r, role='fixe', label=None, size='m', **k): return _d(ax, x, y, r, role, label=label, size=size, **k)
fig, ax = canvas(72)
text(ax, 44, 67, r'$f$ n’est pas un homomorphisme', 'limite')
L = {0: 54, 1: 38, 2: 22}; R = {0: 54, 1: 30}
for k, y in L.items(): disc(ax, 14, y, 5, 'sujet' if k == 0 else 'fixe', str(k), 'l')
for k, y in R.items(): disc(ax, 60, y, 5, 'resultat' if k == 0 else 'limite', str(k), 'l')
arrow(ax, (19.2, 54), (54.8, 54), 'sujet')
arrow(ax, (19.2, 38), (55, 31.5), 'limite'); arrow(ax, (19.2, 22), (55, 28.5), 'limite')
text(ax, 72, 38, 'même image', 'limite', 's', ha='left') if False else text(ax, 77, 40, 'même\nimage', 'limite', 's')
text(ax, 14, 8, r'noyau $= \{0\}$', 'sujet'); text(ax, 60, 8, 'pas injective', 'limite')
text(ax, 14, 63, r'départ', 'fixe', 's'); text(ax, 60, 63, 'arrivée', 'fixe', 's')
save(fig, '48-055')
