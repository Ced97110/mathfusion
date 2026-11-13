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
text(ax, 5, 48, 'premier groupement', 'fixe', 's', ha='left')
text(ax, 5, 26.5, 'second groupement', 'fixe', 's', ha='left')
for y, a, b, c, g, ra, rb in [(34, '$[E,E]$', ZERO, ZERO, '$G$', 'sujet', 'fixe'),
                              (10, '$[E,G]$', HM, [['0', '−2'], ['0', '0']], '$E$', 'sujet', 'sujet')]:
    box(ax, 5, y, 17, 11, ra, label=a)
    arrow(ax, (22, y + 5.5), (36, y + 5.5), 'fixe'); text(ax, 29, y + 9, 'vaut', 'fixe', 's')
    box(ax, 36, y, 17, 11, rb, label='\n'.join('   '.join(r) for r in b))
    arrow(ax, (53, y + 5.5), (67, y + 5.5), 'varie'); text(ax, 60, y + 9, 'avec ' + g, 'varie', 's')
    box(ax, 67, y, 17, 11, 'resultat', label='\n'.join('   '.join(r) for r in c))
text(ax, 75.5, 28, '≠', 'limite', 'xl')
save(fig, '78-005')
