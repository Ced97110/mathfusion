import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(84)
base = dict(sheet=[(0, 0), (22, 0), (22, 15), (0, 15)], p=(4, 3), q=(16, 11))
def put(f):
    return [f(*s) for s in base['sheet']], f(*base['p']), f(*base['q'])
def draw(f, role, lab, tx, ty):
    sh, p, q = put(f)
    poly(ax, sh, role); line(ax, [p, q], 'encre', lw=1.0); disc(ax, *p, 1.1, role); disc(ax, *q, 1.1, role)
ident = lambda x, y: (x + 33, y + 58)
draw(ident, 'sujet', '', 0, 0)
text(ax, 44, 79, 'départ', 'sujet', 's'); text(ax, 51, 64, '5 cm', 'sujet', 's')
glisse = lambda x, y: (x + 3, y + 22)
tourne = lambda x, y: (-(y) + 55, x + 12)
mir = lambda x, y: (-(x) + 85, y + 22)
draw(glisse, 'varie', '', 0, 0); draw(tourne, 'varie', '', 0, 0); draw(mir, 'varie', '', 0, 0)
text(ax, 14, 12, 'glisser', 'varie', 'm'); text(ax, 44, 4, 'tourner', 'varie', 'm'); text(ax, 74, 12, 'retourner', 'varie', 'm')
text(ax, 19, 25.5, '5 cm', 'encre', 's'); text(ax, 70, 25.5, '5 cm', 'encre', 's'); text(ax, 62, 17, '5 cm', 'encre', 's')
arrow(ax, (35, 57), (20, 39), 'fixe', lw=0.8); arrow(ax, (55, 57), (68, 39), 'fixe', lw=0.8); arrow(ax, (44, 57), (44, 37), 'fixe', lw=0.8)
save(fig, '74-015')
