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
fig, ax = canvas(52)
box(ax, 6, 36, 26, 9, 'fixe', label='produit $EG$')
text(ax, 38, 40.5, '−', 'encre', 'l')
box(ax, 44, 36, 26, 9, 'fixe', label='produit $GE$')
arrow(ax, (38, 34), (25, 22), 'varie')
text(ax, 54, 28, 'on le nomme', 'varie', 's')
box(ax, 12, 10, 26, 11, 'sujet', label='$[E,G]$', size='l')
text(ax, 44, 15.5, '=', 'encre', 'l')
box(ax, 50, 10, 14, 11, 'sujet', label='1   0\n0  −1')
save(fig, '78-003')
