import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(62)
u = 2.6; wd = 3 * u
def rect(x, y, w, h, role, lab=None, size='s'):
    poly(ax, [(x, y), (x + w, y), (x + w, y + h), (x, y + h)], role)
    if lab: text(ax, x + w / 2, y + h / 2, lab, role, size)
text(ax, 22, 56, 'deux termes', 'fixe', 's'); text(ax, 66, 56, 'un seul produit', 'fixe', 's')
x1, x2, y0 = 14, 52, 8
rect(x1, y0, wd, 2 * u, 'sujet', '6'); rect(x1, y0 + 2 * u + 3, wd, 5 * u, 'sujet', '15')
rect(x2, y0, wd, 2 * u, 'sujet', '6'); rect(x2, y0 + 2 * u, wd, 5 * u, 'sujet', '15')
text(ax, x1 - 2, y0 + u, r'$a=2$', 'varie', 's', ha='right'); text(ax, x1 - 2, y0 + 2 * u + 3 + 2.5 * u, r'$b=5$', 'varie', 's', ha='right')
brace(ax, x2, x2 + wd, y0 - 1, 'sujet', r'$x-7=3$', True)
line(ax, [(x2 + wd + 2, y0), (x2 + wd + 2, y0 + 7 * u)], 'varie', lw=0.9)
text(ax, x2 + wd + 4, y0 + 3.5 * u, r'$a+b=7$', 'varie', 's', ha='left')
text(ax, x2 + wd / 2, y0 + 7 * u + 4, '21', 'resultat', 'm')
text(ax, x1 + wd / 2, y0 + 7 * u + 7, '21', 'resultat', 'm')
save(fig, '18-038')
