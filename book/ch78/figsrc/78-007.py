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
fig, ax = canvas(62)
text(ax, 44, 58, 'soustraction : pas associative', 'encre', 'm')
box(ax, 3, 42, 38, 10, 'fixe', label='$(8-3)-2=3$')
box(ax, 47, 42, 38, 10, 'fixe', label='$8-(3-2)=7$')
text(ax, 44, 47, '≠', 'limite', 'l')
line(ax, [(3, 36), (85, 36)], 'fixe', lw=0.5)
text(ax, 44, 32, 'le crochet mesure l’écart', 'encre', 'm')
box(ax, 3, 16, 38, 10, 'sujet', label='$[E,G]=H\\neq 0$')
text(ax, 22, 11, 'ne commutent pas', 'limite', 's')
box(ax, 47, 16, 38, 10, 'resultat', label='$[E,E]=0$')
text(ax, 66, 11, 'commutent', 'resultat', 's')
save(fig, '78-007')
