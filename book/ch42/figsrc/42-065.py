import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(75)
box(ax, 4, 52, 30, 14, 'sujet', r'$2+3$', 'l'); box(ax, 54, 52, 30, 14, 'sujet', r'$5$', 'l')
text(ax, 44, 59, r'$=$', 'encre', 'xl')
text(ax, 19, 70, 'côté gauche', 'sujet', 's'); text(ax, 69, 70, 'côté droit', 'sujet', 's')
arrow(ax, (19, 52), (19, 40), 'varie'); text(ax, 22, 46, 'on calcule', 'varie', 's', ha='left')
arrow(ax, (69, 52), (69, 40), 'fixe'); text(ax, 72, 46, 'on lit', 'fixe', 's', ha='left')
box(ax, 4, 26, 30, 14, 'resultat', r'$5$', 'l'); box(ax, 54, 26, 30, 14, 'resultat', r'$5$', 'l')
text(ax, 44, 33, r'$=$', 'resultat', 'xl')
arrow(ax, (44, 26), (44, 16), 'resultat')
box(ax, 18, 4, 52, 12, 'resultat', 'énoncé vrai', 'm')
save(fig, '42-065')
