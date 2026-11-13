import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(58)
xs = [12, 33, 55, 76]; labs = [r'$3+1$', r'$4$', r'$5$', r'$2+3$']; roles = ['sujet', 'fixe', 'fixe', 'sujet']
for x, l, r in zip(xs, labs, roles): box(ax, x - 8, 36, 16, 10, r, l, 'm')
for i, (r, t) in enumerate([('resultat', '='), ('limite', '='), ('resultat', '=')]):
    text(ax, (xs[i] + xs[i + 1]) / 2, 41, t, r, 'l', weight='bold')
text(ax, 44, 52, 'trois égalités à la suite', 'fixe', 's')
text(ax, 44, 31.5, 'vraie        FAUSSE        vraie', 'fixe', 's')
arrow(ax, (12, 33), (76, 33), 'varie', curve=0.0) if False else None
line(ax, [(12, 27), (76, 27)], 'varie', lw=1.2)
arrow(ax, (70, 27), (76, 27), 'varie')
text(ax, 44, 22, 'va de 3+1 à 2+3', 'varie', 's')
box(ax, 14, 4, 60, 11, 'limite', r'$3+1 = 4$ et $2+3 = 5$ : pas égaux', 's')
save(fig, '31-114')
