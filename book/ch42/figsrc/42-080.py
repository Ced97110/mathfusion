import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **kw): return _box(ax, x, y, w, h, role, label=label, size=size, **kw)
fig, ax = canvas(60)
text(ax, 32, 55, r'$n$ est pair', 'sujet', 's'); text(ax, 72, 55, r'$n+1$ est impair', 'autre', 's')
for y, n, role, lab in ((34, '4', 'resultat', 'vrai'), (16, '7', 'limite', 'faux')):
    box(ax, 2, y, 14, 12, 'fixe', r'$n=' + n + '$', 's')
    box(ax, 18, y, 28, 12, role, lab, 'm'); text(ax, 52, y + 6, r'$\Leftrightarrow$', 'encre', 'l'); box(ax, 58, y, 28, 12, role, lab, 'm')
text(ax, 44, 7, 'toujours les deux ensemble', 'sujet', 's')
save(fig, '42-080')
