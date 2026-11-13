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
u = 2.2
rows = [(47, '5', (1, 2), 'sujet'), (33, '13', (2, 3), 'autre'), (12, '65', (4, 7), 'resultat')]
for y0, n, (a, b), role in rows:
    text(ax, 8, y0 + 3, n, role, 'l', weight='bold')
    sq(ax, 20, y0, a * u, role); sq(ax, 20 + a * u + 2, y0, b * u, role)
    text(ax, 64, y0 + 3, f'${a}^2+{b}^2$', role, 'm')
text(ax, 8, 43.3, '×', 'encre', 'l')
text(ax, 8, 30.2, '=', 'encre', 'l')
text(ax, 26, 6, r'$1\times2-2\times3=-4$', 'resultat', 's')
text(ax, 66, 6, r'$1\times3+2\times2=7$', 'resultat', 's')
save(fig, '78-008')
