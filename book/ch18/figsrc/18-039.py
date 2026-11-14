import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
_box = box
def box(ax, x, y, w, h, role='fixe', label=None, size='m', **k): return _box(ax, x, y, w, h, role, label=label, size=size, **k)
fig, ax = canvas(66)
def term(x, y, b, v):
    box(ax, x, y, 19, 9, 'sujet', b); box(ax, x + 19.5, y, 9, 9, 'varie', v)
term(5, 52, r'$(x-7)$', r'$a$'); text(ax, 40, 56.5, '+', 'encre', 'l'); term(46, 52, r'$(x-7)$', r'$b$')
arrow(ax, (44, 50), (44, 38), 'varie'); text(ax, 48, 44, 'retirer le bloc', 'varie', 's', ha='left')
box(ax, 5, 26, 19, 9, 'sujet', r'$(x-7)$')
box(ax, 26, 24, 40, 13, 'varie', fill=False, dash=True)
box(ax, 29, 26, 9, 9, 'varie', r'$a$'); text(ax, 46, 30.5, '+', 'encre', 'l'); box(ax, 54, 26, 9, 9, 'varie', r'$b$')
text(ax, 44, 16, r'$x=9,\ a=4,\ b=1$ : bloc $=2$', 'fixe', 's')
text(ax, 44, 8, r'$2\times4+2\times1=10=2\times5$', 'resultat', 's')
save(fig, '18-039')
