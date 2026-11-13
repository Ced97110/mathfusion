import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def mt(ax, x, y, name, rows, role, nw=9, w=14, h=11):
    """Name then a 2x2 matrix box (all entries in label)."""
    text(ax, x, y + h / 2, name, role, 'm', ha='left')
    box(ax, x + nw, y, w, h, role, label='\n'.join('   '.join(r) for r in rows))

def mta(ax, x, y, name, rows, role, w=14, h=11):
    """2x2 matrix box with its name above."""
    box(ax, x, y, w, h, role, label='\n'.join('   '.join(r) for r in rows))
    text(ax, x + w / 2, y + h + 3, name, role, 'm')

def sq(ax, x, y, s, role):
    poly(ax, [(x, y), (x + s, y), (x + s, y + s), (x, y + s)], role)

ZERO = [['0', '0'], ['0', '0']]
EM = [['0', '1'], ['0', '0']]
GM = [['0', '0'], ['1', '0']]
HM = [['1', '0'], ['0', '−1']]
fig, ax = canvas(58)
U = 11; O = (40, 14)
P = lambda x, y, z=0: iso(x, y, z, O, U)
poly(ax, [P(-0.4, -0.4), P(2.6, -0.4), P(2.6, 2.2), P(-0.4, 2.2)], 'fixe')
text(ax, 66, 13, 'plan', 'fixe', 's')
poly(ax, [P(0, 0), P(2, 0), P(3, 1.5), P(1, 1.5)], 'varie')
arrow(ax, P(0, 0), P(2, 0), 'sujet', lw=1.4)
arrow(ax, P(0, 0), P(1, 1.5), 'varie', lw=1.4)
arrow(ax, P(0, 0, 0), P(0, 0, 3), 'resultat', lw=1.6)
text(ax, P(2, 0)[0] + 3, P(2, 0)[1] - 3, '$u$', 'sujet', 'l')
text(ax, P(1, 1.5)[0] - 3, P(1, 1.5)[1] + 2, '$v$', 'varie', 'l')
text(ax, P(1.5, 0.75)[0] + 1, P(1.5, 0.75)[1] - 1, 'aire 3', 'varie', 's')
text(ax, 40, 53, r'$u\times v$', 'resultat', 'l')
text(ax, 25, 38, 'longueur 3', 'resultat', 's')
save(fig, '78-015')
