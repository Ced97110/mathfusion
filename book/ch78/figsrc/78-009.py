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
rows = [(44, 2, 'deux carrés', 'fixe'), (25, 4, 'quatre carrés : Euler', 'sujet'), (6, 8, 'huit carrés : Degen (1822)', 'sujet')]
for y0, n, lab, role in rows:
    for i in range(n): sq(ax, 4 + i * 6, y0, 4, role)
    text(ax, 4, y0 + 7.5, lab, role, 's', ha='left')
for ya, yb in [(8, 27), (27, 46)]:
    arrow(ax, (72, ya), (72, yb), 'varie'); text(ax, 80, (ya + yb) / 2, '×2', 'varie', 'm')
save(fig, '78-009')
