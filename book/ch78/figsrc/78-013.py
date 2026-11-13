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
fig, ax = canvas(56)
text(ax, 44, 52, 'Frobenius (1878)', 'encre', 'm')
rows = [(40, 1, r'$\mathbb{R}$', 'resultat'), (30, 2, r'$\mathbb{C}$', 'resultat'), (20, 4, r'$\mathbb{H}$', 'resultat'), (4, 8, r'$\mathbb{O}$', 'varie')]
for y0, n, nm, role in rows:
    text(ax, 3, y0 + 3, nm, role, 'l', ha='left')
    text(ax, 12, y0 + 3, str(n), 'encre', 'm', ha='left')
    for i in range(n): box(ax, 20 + 5.5 * i, y0, 4.5, 6, role, r=0.5)
line(ax, [(66, 20), (68, 20), (68, 46), (66, 46)], 'resultat')
text(ax, 77, 33, 'associatif', 'resultat', 's')
line(ax, [(66, 4), (68, 4), (68, 10), (66, 10)], 'varie')
text(ax, 77, 7, 'pas associatif', 'varie', 's')
save(fig, '78-013')
