import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role="fixe", label=None, size="m", **k): return _box(ax, x, y, w, h, role, True, label, size, **k)
fig, ax = canvas(66)
s = 56; x0 = 4
text(ax, x0, 61, r'conjuguées avec $\sin$ : $(1-\sin)(1+\sin)$', 'sujet', 's', ha='left')
box(ax, x0, 48, 0.75 * s, 7, 'sujet', label='0,75', size='s'); text(ax, x0 + 0.75 * s + 2, 51.5, 'produit', 'sujet', 's', ha='left')
box(ax, x0, 39, 0.75 * s, 7, 'resultat', label='0,75', size='s'); text(ax, x0 + 0.75 * s + 2, 42.5, r'$\cos^2 x$', 'resultat', 's', ha='left')
text(ax, 80, 45, '=', 'resultat', 'l')
text(ax, x0, 29, r'conjuguées avec $\cos$ : $(1-\cos)(1+\cos)$', 'limite', 's', ha='left')
box(ax, x0, 16, 0.25 * s, 7, 'limite', label='0,25', size='s'); text(ax, x0 + 0.25 * s + 2, 19.5, 'produit', 'limite', 's', ha='left')
box(ax, x0, 7, 0.75 * s, 7, 'fixe', label='0,75', size='s'); text(ax, x0 + 0.75 * s + 2, 10.5, r'$\cos^2 x$', 'fixe', 's', ha='left')
text(ax, 80, 13, r'$\neq$', 'limite', 'l')
save(fig, '31-127')
