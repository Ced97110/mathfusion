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
text(ax, 44, 48, 'Hamilton cherche (1833-1843)', 'encre', 'm')
rows = [(30, 2, '2 coordonnées (ℂ)', 'réussi', 'resultat'), (17, 3, '3 coordonnées', 'échec', 'limite'), (4, 4, '4 coordonnées (ℍ)', 'réussi', 'resultat')]
for y0, n, lab, res, role in rows:
    text(ax, 3, y0 + 3, lab, 'encre', 'm', ha='left')
    for i in range(n): box(ax, 42 + 7.5 * i, y0, 6, 6, role, r=0.6)
    text(ax, 73, y0 + 3, res, role, 's', ha='left')
save(fig, '78-012')
