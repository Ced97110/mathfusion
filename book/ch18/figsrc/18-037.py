import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(80)
text(ax, 44, 75, "l'élève écrit :", 'fixe', 's')
box(ax, 14, 59, 60, 11, 'autre', r'$6x + 9 = 3(2x + 9)$', 'l')
arrow(ax, (58, 59), (58, 43), 'varie'); text(ax, 62, 51, 'développer', 'varie', 's', ha='left')
box(ax, 14, 31, 60, 11, 'limite', r'$3(2x + 9) = 6x + 27$', 'l')
text(ax, 44, 22, r'$6x + 27 \neq 6x + 9$', 'limite', 'l')
text(ax, 44, 12, r'avec $x = 1$ : $15$ et $33$', 'fixe', 's')
text(ax, 44, 5, 'le développement juge', 'resultat', 's')
save(fig, '18-037')
