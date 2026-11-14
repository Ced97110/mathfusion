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
fig, ax = canvas(60)
S = {a + b + c for a in (0, 1, 4, 9, 16) for b in (0, 1, 4, 9, 16) for c in (0, 1, 4, 9, 16)}
box(ax, 2, 49, 40, 9, 'sujet', label=r'$3=1^2+1^2+1^2$')
box(ax, 46, 49, 40, 9, 'autre', label=r'$5=2^2+1^2+0^2$')
box(ax, 24, 33, 40, 9, 'limite', label=r'$3\times5=15$')
arrow(ax, (22, 49), (36, 42), 'fixe'); arrow(ax, (66, 49), (52, 42), 'fixe')
text(ax, 44, 26, 'sommes de trois carrés', 'encre', 'm')
f = numberline(ax, 8, 76, 11, 8, 18, step=1, every=2)
for v in range(8, 19):
    ok = v in S
    disc(ax, f(v), 16.5, 1.8, 'resultat' if ok else 'limite')
text(ax, f(15), 21.5, r'$15$ : pas une somme', 'limite', 's')
save(fig, '78-010')
